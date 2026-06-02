# Gold Layer Plan

## Oversikt

Gold-laget inneholder analyseklare datasett som er basert på rensede og validerte Silver-tabeller.

Formålet med Gold-laget er å gjøre kollektivtransportdata enklere å bruke for rapportering, SQL-spørringer og videre analyse.

---

## Første planlagte Gold-tabeller

| Gold-tabell | Beskrivelse | Kilde |
|---|---|---|
| route_type_summary | Antall ruter per transporttype | clean_routes |
| operator_route_summary | Antall ruter per operatør | clean_routes + clean_agencies |
| stop_activity_summary | Oversikt over stoppesteder og geografisk dekning | clean_stops |
| route_activity_summary | Oversikt over ruter og planlagte turer | clean_routes + clean_trips |

---

## Første implementasjon

Den første Gold-tabellen som implementeres er:

```text
route_type_summary