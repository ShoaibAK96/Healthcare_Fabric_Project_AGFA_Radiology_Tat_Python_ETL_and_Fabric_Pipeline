import pytest

from radiology_etl.addendum import ExtractionOutcome, classify_addendum_extract


def test_zero_rows_returns_no_data():
    assert classify_addendum_extract(0) == ExtractionOutcome.NO_DATA


def test_positive_rows_are_publishable():
    assert classify_addendum_extract(2) == ExtractionOutcome.READY_TO_PUBLISH


def test_negative_rows_are_rejected():
    with pytest.raises(ValueError):
        classify_addendum_extract(-1)
