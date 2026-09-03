from datetime import date, datetime
from typing import Iterable, Mapping, Any


def validate_columns(actual: Iterable[str], required: Iterable[str]) -> None:
    actual_tuple = tuple(actual)
    required_tuple = tuple(required)
    if actual_tuple != required_tuple:
        missing = [c for c in required_tuple if c not in actual_tuple]
        extra = [c for c in actual_tuple if c not in required_tuple]
        raise ValueError(f"Column contract mismatch; missing={missing}, extra={extra}")


def validate_business_date(rows: Iterable[Mapping[str, Any]], expected: date) -> int:
    count = 0
    for row_number, row in enumerate(rows, start=2):
        value = row.get("ORDER_CREATION_DATE")
        if isinstance(value, datetime):
            row_date = value.date()
        elif isinstance(value, date):
            row_date = value
        else:
            row_date = datetime.fromisoformat(str(value)).date()
        if row_date != expected:
            raise ValueError(f"Row {row_number} is outside business date {expected}")
        if not row.get("ACCESSION_NUMBER"):
            raise ValueError(f"Row {row_number} has no accession number")
        count += 1
    return count
