from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SILVER_DIR = PROJECT_ROOT / "data" / "silver"
REPORTS_DIR = PROJECT_ROOT / "reports"


TABLE_CONFIG = {
    "clean_agencies.parquet": {
        "primary_key": "agency_id",
        "required_columns": ["agency_id", "agency_name"],
    },
    "clean_stops.parquet": {
        "primary_key": "stop_id",
        "required_columns": ["stop_id", "stop_name", "stop_lat", "stop_lon"],
    },
    "clean_routes.parquet": {
        "primary_key": "route_id",
        "required_columns": ["route_id", "agency_id"],
    },
    "clean_trips.parquet": {
        "primary_key": "trip_id",
        "required_columns": ["trip_id", "route_id", "service_id"],
    },
}


def check_required_columns(df: pd.DataFrame, required_columns: list[str]) -> list[str]:
    return [column for column in required_columns if column not in df.columns]


def check_null_values(df: pd.DataFrame, columns: list[str]) -> dict[str, int]:
    result = {}

    for column in columns:
        if column in df.columns:
            result[column] = int(df[column].isna().sum())

    return result


def check_duplicate_keys(df: pd.DataFrame, primary_key: str) -> int:
    if primary_key not in df.columns:
        return -1

    return int(df[primary_key].duplicated().sum())


def check_stop_coordinates(df: pd.DataFrame) -> dict[str, int]:
    if "stop_lat" not in df.columns or "stop_lon" not in df.columns:
        return {
            "invalid_latitude": -1,
            "invalid_longitude": -1,
        }

    invalid_latitude = df[~df["stop_lat"].between(-90, 90)].shape[0]
    invalid_longitude = df[~df["stop_lon"].between(-180, 180)].shape[0]

    return {
        "invalid_latitude": int(invalid_latitude),
        "invalid_longitude": int(invalid_longitude),
    }


def validate_table(file_name: str, config: dict) -> list[str]:
    file_path = SILVER_DIR / file_name
    report_lines = []

    report_lines.append(f"## {file_name}\n")

    if not file_path.exists():
        report_lines.append("Status: File not found\n")
        return report_lines

    df = pd.read_parquet(file_path)

    primary_key = config["primary_key"]
    required_columns = config["required_columns"]

    missing_columns = check_required_columns(df, required_columns)
    null_values = check_null_values(df, required_columns)
    duplicate_keys = check_duplicate_keys(df, primary_key)

    report_lines.append(f"- Rows: {len(df)}")
    report_lines.append(f"- Columns: {len(df.columns)}")
    report_lines.append(f"- Primary key: `{primary_key}`")
    report_lines.append(f"- Missing required columns: {missing_columns if missing_columns else 'None'}")
    report_lines.append(f"- Duplicate primary keys: {duplicate_keys}")

    report_lines.append("\n### Null values in required columns\n")
    for column, count in null_values.items():
        report_lines.append(f"- {column}: {count}")

    if file_name == "clean_stops.parquet":
        coordinate_check = check_stop_coordinates(df)
        report_lines.append("\n### Coordinate checks\n")
        report_lines.append(f"- Invalid latitude values: {coordinate_check['invalid_latitude']}")
        report_lines.append(f"- Invalid longitude values: {coordinate_check['invalid_longitude']}")

    report_lines.append("")
    return report_lines


def build_quality_report() -> str:
    report_lines = [
        "# Silver GTFS Data Quality Report\n",
        "This report summarizes basic data quality checks for the Silver GTFS tables.\n",
    ]

    for file_name, config in TABLE_CONFIG.items():
        report_lines.extend(validate_table(file_name, config))

    return "\n".join(report_lines)


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    report = build_quality_report()
    output_path = REPORTS_DIR / "silver_quality_report.md"
    output_path.write_text(report, encoding="utf-8")

    print(f"Silver quality report written to: {output_path}")


if __name__ == "__main__":
    main()