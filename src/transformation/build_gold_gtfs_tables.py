from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SILVER_DIR = PROJECT_ROOT / "data" / "silver"
GOLD_DIR = PROJECT_ROOT / "data" / "gold"


def build_route_type_summary() -> pd.DataFrame:
    routes_path = SILVER_DIR / "clean_routes.parquet"

    if not routes_path.exists():
        raise FileNotFoundError(f"Missing Silver table: {routes_path}")

    routes_df = pd.read_parquet(routes_path)

    summary_df = (
        routes_df
        .groupby("route_type", dropna=False)
        .size()
        .reset_index(name="route_count")
        .sort_values("route_count", ascending=False)
    )

    return summary_df


def write_gold_table(df: pd.DataFrame, output_name: str) -> None:
    GOLD_DIR.mkdir(parents=True, exist_ok=True)
    output_path = GOLD_DIR / output_name

    df.to_parquet(output_path, index=False)

    print(f"Written Gold table: {output_path}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")


def main() -> None:
    route_type_summary = build_route_type_summary()
    write_gold_table(route_type_summary, "route_type_summary.parquet")


if __name__ == "__main__":
    main()