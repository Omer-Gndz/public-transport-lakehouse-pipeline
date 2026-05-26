from pathlib import Path
import zipfile
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
BRONZE_DIR = PROJECT_ROOT / "data" / "bronze" / "entur_static"
REPORTS_DIR = PROJECT_ROOT / "reports"

IMPORTANT_GTFS_FILES = [
    "agency.txt",
    "stops.txt",
    "routes.txt",
    "trips.txt",
    "stop_times.txt",
    "calendar.txt",
    "calendar_dates.txt",
    "transfers.txt",
]


def find_latest_gtfs_zip() -> Path:
    zip_files = sorted(BRONZE_DIR.glob("*.zip"), reverse=True)

    if not zip_files:
        raise FileNotFoundError(f"No GTFS zip files found in {BRONZE_DIR}")

    return zip_files[0]


def count_rows_in_zip_file(zip_file: zipfile.ZipFile, file_name: str) -> int:
    with zip_file.open(file_name) as file:
        return sum(1 for _ in file) - 1  # subtract header row


def read_sample(zip_file: zipfile.ZipFile, file_name: str, nrows: int = 5) -> pd.DataFrame:
    with zip_file.open(file_name) as file:
        return pd.read_csv(file, nrows=nrows)


def build_profile_report(zip_path: Path) -> str:
    report_lines = []

    report_lines.append("# Raw GTFS Data Profiling Report\n")
    report_lines.append(f"Source file: `{zip_path.name}`\n")
    report_lines.append("## Overview\n")

    with zipfile.ZipFile(zip_path, "r") as zip_file:
        available_files = zip_file.namelist()

        report_lines.append("### Files in GTFS zip\n")
        for file_name in available_files:
            report_lines.append(f"- {file_name}")
        report_lines.append("")

        report_lines.append("## File Profiles\n")

        for file_name in IMPORTANT_GTFS_FILES:
            if file_name not in available_files:
                report_lines.append(f"### {file_name}\n")
                report_lines.append("Status: Not found\n")
                continue

            row_count = count_rows_in_zip_file(zip_file, file_name)
            sample_df = read_sample(zip_file, file_name)

            report_lines.append(f"### {file_name}\n")
            report_lines.append(f"- Rows: {row_count}")
            report_lines.append(f"- Columns: {len(sample_df.columns)}")
            report_lines.append(f"- Column names: {', '.join(sample_df.columns)}\n")

            report_lines.append("Sample rows:\n")
            report_lines.append(sample_df.to_markdown(index=False))
            report_lines.append("\n")

    return "\n".join(report_lines)


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    zip_path = find_latest_gtfs_zip()
    print(f"Profiling GTFS file: {zip_path}")

    report = build_profile_report(zip_path)

    output_path = REPORTS_DIR / "raw_gtfs_profile.md"
    output_path.write_text(report, encoding="utf-8")

    print(f"Profiling report written to: {output_path}")


if __name__ == "__main__":
    main()
    