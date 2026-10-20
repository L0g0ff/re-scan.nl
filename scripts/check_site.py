#!/usr/bin/env python3
"""Check static pages, local links, metadata, image sizes and sitemap."""
import json
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = "https://www.re-scan.nl"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.tags = []
        self.json_blocks = []
        self.json_buffer = None
        self.feed(path.read_text())

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        self.tags.append((tag, attrs))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.json_buffer = ""

    def handle_data(self, data):
        if self.json_buffer is not None:
            self.json_buffer += data

    def handle_endtag(self, tag):
        if tag == "script" and self.json_buffer is not None:
            self.json_blocks.append(self.json_buffer)
            self.json_buffer = None


def main():
    pages = {path.resolve(): Page(path) for path in ROOT.rglob("*.html")}
    errors = []
    canonicals = set()

    def check(condition, message):
        if not condition:
            errors.append(message)

    for path, page in pages.items():
        label = str(path.relative_to(ROOT))
        tags = Counter(tag for tag, _ in page.tags)
        ids = [attrs["id"] for _, attrs in page.tags if "id" in attrs]
        check(tags["h1"] == 1, f"{label}: expected one h1")
        check(tags["main"] == 1, f"{label}: expected one main")
        check(len(ids) == len(set(ids)), f"{label}: duplicate ids")
        check(any(tag == "html" and attrs.get("lang") == "nl"
                  for tag, attrs in page.tags), f"{label}: missing Dutch language")
        check(any(tag == "a" and attrs.get("href") == "#inhoud"
                  for tag, attrs in page.tags), f"{label}: missing skip link")
        if path.name != "404.html":
            canonical = [attrs.get("href") for tag, attrs in page.tags
                         if tag == "link" and attrs.get("rel") == "canonical"]
            expected = ORIGIN + "/" + (label[:-10] if label.endswith("index.html") else label)
            check(canonical == [expected], f"{label}: incorrect canonical")
            canonicals.update(canonical)
            check(any(tag == "meta" and attrs.get("property") == "og:url"
                      and attrs.get("content") == expected for tag, attrs in page.tags),
                  f"{label}: incorrect social URL")
        for block in page.json_blocks:
            try:
                json.loads(block)
            except ValueError as error:
                errors.append(f"{label}: invalid structured data: {error}")
        for tag, attrs in page.tags:
            if tag == "img":
                check(bool(attrs.get("alt")), f"{label}: missing image description")
                check(all(attrs.get(key, "").isdigit() and int(attrs[key]) > 0
                          for key in ("width", "height")), f"{label}: missing image dimensions")
            check(not (tag == "script" and attrs.get("src")), f"{label}: unexpected runtime JavaScript")
            for attribute in ("href", "src"):
                url = urlsplit(attrs.get(attribute, ""))
                if url.scheme or url.netloc or not (url.path or url.fragment):
                    continue
                target = ((ROOT / unquote(url.path.lstrip("/"))) if url.path.startswith("/")
                          else (path.parent / unquote(url.path))) if url.path else path
                if target.is_dir():
                    target /= "index.html"
                target = target.resolve()
                check(target.is_file(), f"{label}: missing local target {attrs[attribute]}")
                if url.fragment and target in pages:
                    check(any(a.get("id") == unquote(url.fragment) for _, a in pages[target].tags),
                          f"{label}: missing anchor {attrs[attribute]}")
    sitemap = ElementTree.parse(ROOT / "sitemap.xml")
    sitemap_urls = {node.text for node in sitemap.findall(".//{*}loc")}
    check(sitemap_urls == canonicals, "Sitemap and canonical page URLs differ")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"OK: {len(pages)} pages; local links, anchors, landmarks, metadata, images and sitemap.")


if __name__ == "__main__":
    main()
