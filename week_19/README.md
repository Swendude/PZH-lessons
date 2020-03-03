# Eindopdracht

Een webapplicatie die willekeurige persoonsprofielen kan genereren. 

Voorbeelden:
- Willekeurige burger
- Willekeurig fantasy character
- Willekeurige beleidsambtenaar

De webapplicatie kent twee pagina's:
## "/" (homepage)
- Op deze pagina krijg je in een mooie interface verschillende informatie over de gegenereerde persoon te zien
- Het moet mogelijk zijn om attributen te 'locken' in de url door gebruik te maken van url parameters. (Zie: https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object)
Bijvoorbeeld:
`/?name=swen` zal altijd een persoon met de naam swen genereren (je mag zelf je attributen kiezen natuurlijk)

## "/attributes"
- Op deze pagina moet een lijst beschikbaar zijn waarin alle mogelijk waarden voor je attributen staan.