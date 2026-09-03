from datetime import date
import pytest
from radiology_etl.validation import validate_columns, validate_business_date


def test_exact_column_contract():
    validate_columns(["A", "B"], ["A", "B"])
    with pytest.raises(ValueError):
        validate_columns(["B", "A"], ["A", "B"])


def test_business_date_and_accession():
    rows = [{"ACCESSION_NUMBER": "SYN-1", "ORDER_CREATION_DATE": "2026-01-15T08:00:00"}]
    assert validate_business_date(rows, date(2026, 1, 15)) == 1


def test_rejects_wrong_date():
    rows = [{"ACCESSION_NUMBER": "SYN-1", "ORDER_CREATION_DATE": "2026-01-14T23:59:59"}]
    with pytest.raises(ValueError):
        validate_business_date(rows, date(2026, 1, 15))
