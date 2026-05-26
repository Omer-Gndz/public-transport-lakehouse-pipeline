# Silver Layer Plan

## Oversikt

Dette dokumentet beskriver den første planen for Silver-laget i Public Transport Lakehouse Pipeline.

Silver-laget skal inneholde rensede, standardiserte og validerte datasett basert på rå GTFS-data fra Bronze-laget.

---

## Første prioriterte datasett

I første versjon fokuserer vi på følgende GTFS-filer:

| Bronze-fil | Silver-tabell | Begrunnelse |
|---|---|---|
| agency.txt | clean_agencies | Inneholder transportoperatører |
| stops.txt | clean_stops | Inneholder stoppesteder og geografisk informasjon |
| routes.txt | clean_routes | Inneholder ruter og linjer |
| trips.txt | clean_trips | Inneholder planlagte turer |

---

## Midlertidig utsatt datasett

| Bronze-fil | Begrunnelse |
|---|---|
| stop_times.txt | Svært stor fil med mange millioner rader. Behandles etter at grunnleggende referansedata er renset. |

---

## Foreslåtte datakvalitetskontroller

### agency.txt

- agency_id skal ikke være tom
- agency_name skal ikke være tom
- dupliserte agency_id-er skal identifiseres

### stops.txt

- stop_id skal ikke være tom
- stop_name skal ikke være tom
- stop_lat og stop_lon skal ha gyldige koordinater
- dupliserte stop_id-er skal identifiseres

### routes.txt

- route_id skal ikke være tom
- agency_id skal finnes
- route_short_name eller route_long_name bør finnes
- dupliserte route_id-er skal identifiseres

### trips.txt

- trip_id skal ikke være tom
- route_id skal ikke være tom
- service_id skal ikke være tom
- dupliserte trip_id-er skal identifiseres

---

## Planlagt output i Silver-laget

```text
data/silver/
├── clean_agencies.parquet
├── clean_stops.parquet
├── clean_routes.parquet
└── clean_trips.parquet
