"""Public-safe addendum extraction decisions."""

from enum import Enum


class ExtractionOutcome(str, Enum):
    READY_TO_PUBLISH = "READY_TO_PUBLISH"
    NO_DATA = "NO_DATA"


def classify_addendum_extract(row_count: int) -> ExtractionOutcome:
    """Decide whether a validated addendum workbook should be published."""
    if row_count < 0:
        raise ValueError("row_count cannot be negative")
    if row_count == 0:
        return ExtractionOutcome.NO_DATA
    return ExtractionOutcome.READY_TO_PUBLISH
