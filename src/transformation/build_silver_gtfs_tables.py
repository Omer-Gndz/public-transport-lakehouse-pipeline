from pathlib import Path
import zipfile
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
BRONZE_DIR = PROJECT_ROOT / "data" / "bronze" / "entur_static"
SILVER_DIR = PROJECT_ROOT / "data" / "silver"


GTFS_TABLES = {
    "agency.txt": "clean_agencies.parquet",
    "stops.txt": "clean_stops.parquet",
    "routes.txt": "clean_routes.parquet",
    "trips.txt": "clean_trips.parquet",
}


def find_latest_gtfs_zip() -> Path:
    zip_files = sorted(BRONZE_DIR.glob("*.zip"), reverse=True)

    if not zip_files:
        raise FileNotFoundError(f"No GTFS zip files found in {BRONZE_DIR}")

    return zip_files[0]


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def remove_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = standardize_column_names(df)
    df = remove_duplicate_rows(df)
    return df


def read_gtfs_file(zip_file: zipfile.ZipFile, file_name: str) -> pd.DataFrame:
    with zip_file.open(file_name) as file:
        return pd.read_csv(file, low_memory=False)


def write_silver_table(df: pd.DataFrame, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_file, index=False)


def main() -> None:
    zip_path = find_latest_gtfs_zip()
    print(f"Using Bronze GTFS file: {zip_path}")

    with zipfile.ZipFile(zip_path, "r") as zip_file:
        available_files = zip_file.namelist()

        for source_file, output_name in GTFS_TABLES.items():
            if source_file not in available_files:
                print(f"Skipping {source_file}: file not found")
                continue

            print(f"Processing {source_file}")

            raw_df = read_gtfs_file(zip_file, source_file)
            clean_df = clean_dataframe(raw_df)

            output_path = SILVER_DIR / output_name
            write_silver_table(clean_df, output_path)

            print(
                f"Written {output_path} "
                f"with {len(clean_df)} rows and {len(clean_df.columns)} columns"
            )


if __name__ == "__main__":
    main()
    