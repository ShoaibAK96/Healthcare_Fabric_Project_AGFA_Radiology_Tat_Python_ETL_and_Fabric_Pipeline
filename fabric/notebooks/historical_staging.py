"""One-time historical staging reference.

This public version intentionally stops after audit. It does not append staging
data into the production Delta table.
"""

HISTORICAL_INCOMING = "Files/Radiology_TAT/Historical_Incoming"
STAGING_TABLE = "analytics.stg_radiology_tat_historical_onetime"
BATCH_SIZE = 50_000


def audit_historical_staging(frame, expected_rows: int):
    actual_rows = frame.count()
    distinct_hashes = frame.select("record_hash_sha256").distinct().count()
    duplicate_rows = actual_rows - distinct_hashes
    missing_accessions = frame.filter("ACCESSION_NUMBER IS NULL").count()
    if actual_rows != expected_rows or duplicate_rows or missing_accessions:
        raise RuntimeError(
            f"Historical audit failed: rows={actual_rows}, duplicates={duplicate_rows}, "
            f"missing_accessions={missing_accessions}"
        )
    return {"status": "STAGING_AUDIT_PASSED", "rows": actual_rows}


# GOVERNANCE BOUNDARY: no production-promotion function is provided.
