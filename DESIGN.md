# Re-Scan: KISS

Doel: bezoekers begrijpen het aanbod en kunnen rechtstreeks contact opnemen.
De website blijft statische HTML en CSS, zonder runtime-JavaScript of buildstap.

## Vormgeving

- Brede presentatie met een maximale inhoudsbreedte van 1320 px.
- Artikelen behouden een leeskolom van maximaal 760 px.
- Eén systeemlettertype voor alle tekst; geen externe fontdownloads.
- Witte basis, tekst `#18251d`, groene links `#236e45`.
- Primaire knoppen: fris limegroen `#c2ec83` met donkere tekst `#153f31`.
- Een zachte groene achtergrond in de opening en een donkergroene sensor-audit
  zorgen voor kleur en contrast. De contactstrook behoudt `#e9f0e5`.
- Het lichtere merkgroen `#54b435` blijft onderdeel van de illustratie.
- Grote koppen, korte teksten, dunne lijnen en weinig decoratie.
- De opening vult samen met de header minimaal het eerste scherm. De kop is
  'Monitoring moet je waarschuwen. Niet je ...'; de klantlogo's verschijnen
  pas bij scrollen.
- Gebruik de variabelen in `css/style.css` voor kleuren en breedte.
- De OpenAI-referentie van de gebruiker bepaalt de gewenste ruime presentatie.
  De statische Apple-studie uit awesome-design-md is aanvullend geraadpleegd
  voor typografische hiërarchie en rustige secties, niet als merksjabloon.

## Beweging

De SVG op de homepage illustreert Meten, Signaleren en Ingrijpen.
Het is geen live statusweergave. Eén CSS-sequentie van vier seconden tekent de
lijn en markeert een signaal. Daarna loopt elke vijf seconden een puls over de
lijn; bij Signaleren kleurt het punt kort amber. Alle tekst en
contactmogelijkheden zijn vanaf het begin zichtbaar.

Op verzoek heeft de homepage enkele blikvangers, allemaal in CSS: de
PRTG-screenshot staat schuin en kantelt vlak bij het scrollen, secties schuiven
in beeld, prijskaarten lichten op bij hover. Scrollgestuurde delen staan binnen
`@supports (animation-timeline: view())`; andere browsers tonen de vaste opmaak.

De kop wisselt op verzoek elke vier seconden tussen eindgebruiker, collega,
opdrachtgever, manager, directie, partner en klant. De woorden staan in
hetzelfde gridvak: het langste woord bepaalt de breedte, zodat de kop niet
verspringt. De screenreader krijgt één vaste, volledige zin.

Bij `prefers-reduced-motion: reduce` staat de illustratie direct in de eindstand
en blijft de kop op 'eindgebruiker' staan;
puls, scrolleffecten en hoverbeweging staan uit.

## Onderdelen

- Gedeelde header met altijd zichtbare navigatie, ook op mobiel.
- Een vaste rij klantlogo's onder de opening, lokaal geladen. Met een muis zijn
  ze grijs en krijgen ze kleur bij hover; op aanraakschermen altijd in kleur.
  Op kleine schermen lopen de logo's over meerdere rijen; geen carrousel.
- Eén primaire contactactie, met bellen als alternatief.
- Drie flexibele prijskaarten met dezelfde opbouw en een eigen mailonderwerp.
- Dezelfde knoppen, focusmarkering en footer op homepage en kennisbank.
- Elk document heeft een hoofdinhoud en een overslaanlink.
- Afbeeldingen hebben afmetingen; codeblokken zijn met het toetsenbord bereikbaar.

## Inhoud en onderhoud

Prijzen en dienstomschrijvingen staan op de homepage, op de dienstpagina, in de
JSON-LD van beide en in `llms.txt`. Pas ze op alle vier de plekken aan.
Geen analytics, trackers of cookies.

Behoud bestaande URL's. Voeg geen klantnamen, resultaten, garanties,
btw-aannames of voorwaarden toe zonder inhoudelijke bevestiging.
Wijzig gedeelde navigatie en footer consequent in alle HTML-documenten.
Gebruik `python3 scripts/check_site.py` en controleer daarna de pagina's in een
browser op 320, 390, 768, 1024 en 1440 px, met en zonder beweging.
