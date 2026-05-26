from pathlib import Path
from datetime import datetime
import requests


DATA_URL = "https://storage.googleapis.com/marduk-production/outbound/gtfs/rb_norway-aggregated-gtfs.zip"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
BRONZE_DIR = PROJECT_ROOT / "data" / "bronze" / "entur_static"


def download_file(url: str, output_path: Path) -> None:
    """
    Download a file from a URL and save it to the given output path.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Starter nedlasting fra: {url}")

    response = requests.get(url, timeout=120)
    response.raise_for_status()

    output_path.write_bytes(response.content)

    print(f"Fil lagret til: {output_path}")
    print(f"Filstørrelse: {output_path.stat().st_size / 1024 / 1024:.2f} MB")


def main() -> None:
    run_date = datetime.now().strftime("%Y-%m-%d")
    output_file = BRONZE_DIR / f"entur_gtfs_norway_{run_date}.zip"

    download_file(DATA_URL, output_file)


if __name__ == "__main__":
    main()
    