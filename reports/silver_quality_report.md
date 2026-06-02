# Silver GTFS Data Quality Report

This report summarizes basic data quality checks for the Silver GTFS tables.

## clean_agencies.parquet

- Rows: 74
- Columns: 5
- Primary key: `agency_id`
- Missing required columns: None
- Duplicate primary keys: 0

### Null values in required columns

- agency_id: 0
- agency_name: 0

## clean_stops.parquet

- Rows: 142752
- Columns: 11
- Primary key: `stop_id`
- Missing required columns: None
- Duplicate primary keys: 0

### Null values in required columns

- stop_id: 0
- stop_name: 0
- stop_lat: 0
- stop_lon: 0

### Coordinate checks

- Invalid latitude values: 0
- Invalid longitude values: 0

## clean_routes.parquet

- Rows: 4427
- Columns: 9
- Primary key: `route_id`
- Missing required columns: None
- Duplicate primary keys: 0

### Null values in required columns

- route_id: 0
- agency_id: 0

## clean_trips.parquet

- Rows: 392022
- Columns: 7
- Primary key: `trip_id`
- Missing required columns: None
- Duplicate primary keys: 0

### Null values in required columns

- trip_id: 0
- route_id: 0
- service_id: 0
