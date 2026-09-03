import argparse
import csv
from datetime import date, datetime, timedelta
from pathlib import Path

from .config import load_settings
from .excel_writer import write_workbook_atomic
from .oracle_source import extract_rows
from .validation import validate_business_date, validate_columns
from .hashing import sha256_file


def csv_rows(path: str | Path):
    with Path(path).open(encoding="utf-8", newline="") as stream:
        yield from csv.DictReader(stream)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--business-date", type=date.fromisoformat)
    parser.add_argument("--source-csv", help="Use synthetic CSV instead of Oracle")
    args = parser.parse_args()

    settings = load_settings(args.config)
    business_date = args.business_date or (datetime.now().date() - timedelta(days=1))
    rows = list(csv_rows(args.source_csv)) if args.source_csv else list(extract_rows(settings.sql_file, business_date))
    validate_columns(rows[0].keys() if rows else settings.required_columns, settings.required_columns)
    validate_business_date(rows, business_date)
    filename = f"{settings.filename_prefix}_{business_date.isoformat()}.xlsx"
    output = write_workbook_atomic(rows, settings.required_columns, settings.worksheet_name, settings.output_directory / filename)
    print({"status": "SUCCESS", "rows": len(rows), "file": output.name, "sha256": sha256_file(output)})


if __name__ == "__main__":
    main()
