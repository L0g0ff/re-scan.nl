# Re-Scan Monitor Solutions

Statische Nederlandstalige website voor PRTG-monitoring, consultancy, hosting en training.
HTML en CSS, zonder buildstap, runtime-JavaScript of externe lettertypen.

## Lokaal bekijken

Start vanuit deze map:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765`. Stop de server met Ctrl+C.

## Structuur

- `index.html`: homepage, diensten, tarieven, kennisbankselectie en contact.
- `blog/`: overzicht en twaalf artikelen met bestaande URL's.
- `css/style.css`: gedeelde opmaak en de monitoringanimatie.
- `css/blog.css`: leeskolom, artikeloverzicht, zijbalk en codeblokken.
- `images/`: favicon, screenshots en lokaal opgeslagen klantlogo's. Herkomst van de logo's staat in `images/clients/SOURCES.md`.
- `404.html`: foutpagina met absolute links voor ontbrekende URL's.
- `sitemap.xml`, `robots.txt`, `CNAME`, `_config.yml`: vindbaarheid en hostingconfiguratie.
- `DESIGN.md`: afspraken voor vormgeving en KISS.
- `scripts/check_site.py`: controle zonder aanvullende dependencies.

## Onderhoud en controles

```sh
python3 scripts/check_site.py
git diff --check
```

De controle valideert lokale links, ankers, paginahoofdstructuur, canonical-URL's,
Open Graph-URL's, JSON-LD, afbeeldingsafmetingen en de sitemap.
Controleer visuele wijzigingen daarnaast in een browser op mobiel, tablet en desktop.
Test toetsenbordbediening, lange codeblokken en de instelling voor minder beweging.

De monitoringillustratie op de homepage is een SVG met één CSS-animatie van vier
seconden. Daarna blijft deze stilstaan. Bij `prefers-reduced-motion: reduce` verschijnt
de eindstand direct. Het is een illustratie, geen live beschikbaarheidsmeting.
Alle navigatie en contactlinks functioneren zonder JavaScript.

De kop wisselt met een CSS-animatie elke vier seconden van woord, in een cyclus
van 28 seconden. Met 'Tekst stilzetten' pauzeer je het wisselen. Bij minder
beweging blijft 'eindgebruiker' staan. De tekst voor screenreaders blijft stabiel.

De gedeelde header en footer staan rechtstreeks in de HTML-documenten. Pas die
bij wijzigingen consequent aan. Kleuren en breedte staan in `:root` in `css/style.css`.
Tarieven staan op de homepage; publicatie- en wijzigingsdatums van artikelen staan
in de JSON-LD. Werk sitemapdatums bij wanneer een pagina daadwerkelijk verandert.

Contact werkt via `mailto:` en `tel:`. Er is geen contactformulier of formulierbackend.
Blogartikelen bevatten deels externe Unsplash-afbeeldingen; de homepage doet geen
externe assetverzoeken. Lokale linkcontroles verifiëren geen externe afbeeldingen.

## Hosting

De repository is ingericht voor GitHub Pages met `www.re-scan.nl` als eigen domein.
Lokaal werken publiceert niets. Een push of wijziging aan hosting vereist een
afzonderlijke opdracht.

`_redirects` bevat oude WordPress-migratieregels. Dit bestand wordt niet door de
lokale Python-server uitgevoerd. Controleer vóór publicatie op de daadwerkelijke
hosting of de oude URL's correct doorverwijzen; een aanwezig bestand bewijst dat niet.

© 2026 Re-Scan Monitor Solutions.
