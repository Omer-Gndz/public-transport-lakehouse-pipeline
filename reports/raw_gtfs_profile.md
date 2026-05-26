# Raw GTFS Data Profiling Report

Source file: `entur_gtfs_norway_2026-05-26.zip`

## Overview

### Files in GTFS zip

- feed_info.txt
- calendar.txt
- trips.txt
- shapes.txt
- calendar_dates.txt
- stops.txt
- transfers.txt
- stop_times.txt
- routes.txt
- agency.txt

## File Profiles

### agency.txt

- Rows: 74
- Columns: 5
- Column names: agency_id, agency_name, agency_url, agency_timezone, agency_phone

Sample rows:

| agency_id            | agency_name                   | agency_url                 | agency_timezone   | agency_phone    |
|:---------------------|:------------------------------|:---------------------------|:------------------|:----------------|
| AKT:Authority:AKT_ID | Agder Kollektivtrafikk AS     | https://www.akt.no         | Europe/Oslo       | +4738038300     |
| ASH:Authority:1      | Arctic Sea Hotel & Apartments | https://arcticseahotel.no/ | Europe/Oslo       | nan             |
| ATB:Authority:2      | AtB                           | https://www.atb.no         | Europe/Oslo       | nan             |
| ATU:Authority:1      | Ålesund Turvogn Service       | https://www.turvogna.no/   | Europe/Oslo       | nan             |
| AVI:Authority:Avinor | Avinor                        | https://www.avinor.no      | Europe/Oslo       | 0047 815 30 550 |


### stops.txt

- Rows: 142752
- Columns: 11
- Column names: stop_id, stop_name, stop_lat, stop_lon, stop_desc, location_type, parent_station, wheelchair_boarding, stop_timezone, vehicle_type, platform_code

Sample rows:

| stop_id         | stop_name          |   stop_lat |   stop_lon |   stop_desc |   location_type | parent_station      |   wheelchair_boarding |   stop_timezone |   vehicle_type |   platform_code |
|:----------------|:-------------------|-----------:|-----------:|------------:|----------------:|:--------------------|----------------------:|----------------:|---------------:|----------------:|
| NSR:Quay:100140 | Rennes kryss       |    58.0209 |    7.41299 |         nan |             nan | NSR:StopPlace:58401 |                   nan |             nan |            700 |             nan |
| NSR:Quay:100141 | Fjellheim snuplass |    58.3298 |    7.59847 |         nan |             nan | NSR:StopPlace:58402 |                   nan |             nan |            700 |             nan |
| NSR:Quay:100157 | Frikstad øst       |    58.5216 |    7.92536 |         nan |             nan | NSR:StopPlace:58414 |                   nan |             nan |            700 |             nan |
| NSR:Quay:100162 | Vigeland sentrum   |    58.0847 |    7.30343 |         nan |             nan | NSR:StopPlace:58419 |                   nan |             nan |            700 |             nan |
| NSR:Quay:100163 | Vigeland sentrum   |    58.0848 |    7.30303 |         nan |             nan | NSR:StopPlace:58419 |                   nan |             nan |            700 |             nan |


### routes.txt

- Rows: 4427
- Columns: 9
- Column names: agency_id, route_id, route_short_name, route_long_name, route_type, route_desc, route_url, route_color, route_text_color

Sample rows:

| agency_id            | route_id      |   route_short_name | route_long_name               |   route_type |   route_desc |   route_url |   route_color | route_text_color   |
|:---------------------|:--------------|-------------------:|:------------------------------|-------------:|-------------:|------------:|--------------:|:-------------------|
| AKT:Authority:AKT_ID | AKT:Line:100  |                100 | Arendal-Kristiansand          |          701 |          nan |         nan |             0 | FFFF00             |
| AKT:Authority:AKT_ID | AKT:Line:101  |                101 | Eydehavn-Arendal-Grimstad N/S |          704 |          nan |         nan |             0 | FFFF00             |
| AKT:Authority:AKT_ID | AKT:Line:1010 |                 10 | Sykehuset - Kvadraturen       |          704 |          nan |         nan |             0 | FFFF00             |
| AKT:Authority:AKT_ID | AKT:Line:1012 |                 12 | Kjos haveby - Justvik         |          704 |          nan |         nan |             0 | FFFF00             |
| AKT:Authority:AKT_ID | AKT:Line:1013 |                 13 | Lokalbuss Grimsmyra - Lund    |          704 |          nan |         nan |             0 | FFFF00             |


### trips.txt

- Rows: 392022
- Columns: 7
- Column names: route_id, trip_id, service_id, trip_headsign, direction_id, shape_id, wheelchair_accessible

Sample rows:

| route_id      | trip_id                                                 | service_id       | trip_headsign                    |   direction_id | shape_id                    |   wheelchair_accessible |
|:--------------|:--------------------------------------------------------|:-----------------|:---------------------------------|---------------:|:----------------------------|------------------------:|
| AKT:Line:1031 | AKT:ServiceJourney:11760_8222_44_117840_120120_40000859 | AKT:DayType:64_1 | Kristiansand via Baneheitunnelen |              1 | AKT:JourneyPattern:65882_1  |                     nan |
| AKT:Line:1031 | AKT:ServiceJourney:11761_8242_44_125040_127320_40000859 | AKT:DayType:64_1 | Kristiansand via Baneheitunnelen |              1 | AKT:JourneyPattern:65882_1  |                     nan |
| AKT:Line:1012 | AKT:ServiceJourney:12744_9382_45_147720_150420_3950120  | AKT:DayType:63_1 | Kjos haveby                      |              1 | AKT:JourneyPattern:110503_1 |                     nan |
| AKT:Line:1012 | AKT:ServiceJourney:12745_9402_45_151320_154020_3950120  | AKT:DayType:63_1 | Kjos haveby                      |              1 | AKT:JourneyPattern:110503_1 |                     nan |
| AKT:Line:1012 | AKT:ServiceJourney:12746_9412_45_154920_157620_3950120  | AKT:DayType:63_1 | Kjos haveby                      |              1 | AKT:JourneyPattern:110503_1 |                     nan |


### stop_times.txt

- Rows: 9749760
- Columns: 9
- Column names: trip_id, stop_id, arrival_time, departure_time, stop_sequence, stop_headsign, pickup_type, drop_off_type, shape_dist_traveled

Sample rows:

| trip_id                                                 | stop_id         | arrival_time   | departure_time   |   stop_sequence |   stop_headsign |   pickup_type |   drop_off_type |   shape_dist_traveled |
|:--------------------------------------------------------|:----------------|:---------------|:-----------------|----------------:|----------------:|--------------:|----------------:|----------------------:|
| AKT:ServiceJourney:11760_8222_44_117840_120120_40000859 | NSR:Quay:103541 | 16:22:00       | 16:22:00         |               1 |             nan |           nan |               1 |                     0 |
| AKT:ServiceJourney:11760_8222_44_117840_120120_40000859 | NSR:Quay:41032  | 16:23:00       | 16:23:00         |               2 |             nan |           nan |             nan |                   973 |
| AKT:ServiceJourney:11760_8222_44_117840_120120_40000859 | NSR:Quay:41041  | 16:24:00       | 16:24:00         |               3 |             nan |           nan |             nan |                  1482 |
| AKT:ServiceJourney:11760_8222_44_117840_120120_40000859 | NSR:Quay:41278  | 16:25:00       | 16:25:00         |               4 |             nan |           nan |             nan |                  1869 |
| AKT:ServiceJourney:11760_8222_44_117840_120120_40000859 | NSR:Quay:38870  | 16:25:00       | 16:25:00         |               5 |             nan |           nan |             nan |                  2336 |


### calendar.txt

- Rows: 4241
- Columns: 10
- Column names: service_id, monday, tuesday, wednesday, thursday, friday, saturday, sunday, start_date, end_date

Sample rows:

| service_id        |   monday |   tuesday |   wednesday |   thursday |   friday |   saturday |   sunday |   start_date |   end_date |
|:------------------|---------:|----------:|------------:|-----------:|---------:|-----------:|---------:|-------------:|-----------:|
| AKT:DayType:100_1 |        1 |         0 |           1 |          1 |        1 |          0 |        0 |     20260516 |   20260927 |
| AKT:DayType:101_1 |        1 |         1 |           1 |          1 |        1 |          1 |        0 |     20260515 |   20261004 |
| AKT:DayType:102_1 |        0 |         0 |           0 |          0 |        1 |          0 |        0 |     20260509 |   20261008 |
| AKT:DayType:103_1 |        1 |         1 |           1 |          1 |        1 |          0 |        0 |     20260813 |   20261004 |
| AKT:DayType:104_1 |        1 |         1 |           1 |          1 |        1 |          0 |        0 |     20260813 |   20260927 |


### calendar_dates.txt

- Rows: 271477
- Columns: 3
- Column names: service_id, date, exception_type

Sample rows:

| service_id        |     date |   exception_type |
|:------------------|---------:|-----------------:|
| AKT:DayType:100_1 | 20260525 |                2 |
| AKT:DayType:100_1 | 20260622 |                2 |
| AKT:DayType:100_1 | 20260624 |                2 |
| AKT:DayType:100_1 | 20260625 |                2 |
| AKT:DayType:100_1 | 20260626 |                2 |


### transfers.txt

- Rows: 69105
- Columns: 5
- Column names: from_stop_id, from_trip_id, to_stop_id, to_trip_id, transfer_type

Sample rows:

| from_stop_id   | from_trip_id                                          | to_stop_id     | to_trip_id                                             |   transfer_type |
|:---------------|:------------------------------------------------------|:---------------|:-------------------------------------------------------|----------------:|
| NSR:Quay:43570 | AKT:ServiceJourney:17995_11_24_47160_50100_3911783    | NSR:Quay:43570 | AKT:ServiceJourney:57370_21_25_48600_50520_1072401     |               1 |
| NSR:Quay:40036 | AKT:ServiceJourney:36846_12_33_87840_90540_1072161    | NSR:Quay:40036 | AKT:ServiceJourney:36849_42_5_89160_89460_1072171      |               1 |
| NSR:Quay:40036 | AKT:ServiceJourney:36865_152_33_99960_103260_1072161  | NSR:Quay:40036 | AKT:ServiceJourney:36874_232_34_101400_104400_1072151  |               1 |
| NSR:Quay:38842 | AKT:ServiceJourney:52709_271_55_99000_101760_40001540 | NSR:Quay:38842 | AKT:ServiceJourney:52830_3333_50_102600_105300_3950341 |               1 |
| NSR:Quay:44438 | AKT:ServiceJourney:70517_12_22_49800_52620_3911093    | NSR:Quay:44438 | AKT:ServiceJourney:16649_122_59_54600_57780_3911003    |               1 |

