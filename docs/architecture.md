# Prosjektarkitektur

## Oversikt

Dette prosjektet følger en Databricks-inspirert lakehouse-arkitektur for behandling av norske kollektivtransportdata fra Entur.

Målet er å bygge en profesjonell data engineering-pipeline som henter inn rådata, lagrer dem i et Bronze-lag, transformerer og validerer dem i et Silver-lag, og produserer analyseklare datasett i et Gold-lag.

---

## Datakilde

Prosjektet bruker offentlige kollektivtransportdata fra Entur.

Første versjon av prosjektet fokuserer på statiske data, for eksempel:

- stoppesteder
- ruter
- turer
- rutetabeller

Senere kan prosjektet utvides med sanntidsdata, for eksempel kjøretøyposisjoner og oppdaterte avgangs- og ankomsttider.

---

## Overordnet dataflyt

```text
Entur data source
        ↓
Ingestion
        ↓
Bronze layer
        ↓
Transformation
        ↓
Silver layer
        ↓
Validation
        ↓
Gold layer
        ↓
SQL / Analytics