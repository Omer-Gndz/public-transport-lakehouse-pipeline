# Public Transport Lakehouse Pipeline

## Prosjektoversikt

Public Transport Lakehouse Pipeline er et data engineering-porteføljeprosjekt som henter inn, validerer, transformerer og modellerer norske kollektivtransportdata ved hjelp av en Databricks-inspirert lakehouse-arkitektur.

Prosjektet følger en Bronze-, Silver- og Gold-lagstruktur og viser moderne data engineering-prinsipper som data ingestion, datakvalitetskontroller, SQL-modellering, pipeline-automatisering, logging, dokumentasjon og profesjonell GitHub-workflow.

## Datakilde

Prosjektet bruker offentlige kollektivtransportdata fra Entur, som er Norges nasjonale plattform for kollektivtransportdata.

Første fokus:

- statiske rutetabell-data
- stoppesteder
- ruter
- turer

Mulig videreutvikling:

- sanntidsdata for kjøretøy
- oppdaterte avgangs- og ankomsttider
- forsinkelsesanalyse

## Arkitektur

Prosjektet er organisert i tre lakehouse-inspirerte datalag:

### Bronze-lag

Bronze-laget inneholder rådata slik de hentes fra den eksterne datakilden. Dataene lagres uten forretningsmessige transformasjoner.

### Silver-lag

Silver-laget inneholder rensede, standardiserte og validerte data som er klare for videre modellering.

### Gold-lag

Gold-laget inneholder analyseklare tabeller som kan brukes til rapportering, SQL-spørringer og forretningsanalyse.

## Prosjektstruktur

```text
public-transport-lakehouse-pipeline/
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── docs/
├── logs/
├── reports/
├── sql/
├── src/
│   ├── ingestion/
│   ├── transformation/
│   ├── validation/
│   └── utils/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
