"""Public-safe Fabric notebook source.

Paste sections into a Fabric notebook or convert to .ipynb. The deployment must
provide approved Lakehouse paths and table names. Spark/notebookutils are
available in the Fabric runtime and intentionally are not local dependencies.
"""

from pyspark.sql import functions as F

INCOMING_PATH = "Files/Radiology_TAT/Incoming"
ARCHIVE_PATH = "Files/Radiology_TAT/Archive"
DATA_TABLE = "analytics.fact_radiology_tat"
FILE_LOG_TABLE = "analytics.fact_radiology_tat_file_log"
ERROR_LOG_TABLE = "analytics.fact_radiology_tat_error_log"


def choose_load_action(file_hash: str, business_date):
    exact_success = (
        spark.table(FILE_LOG_TABLE)
        .filter((F.col("file_hash_sha256") == file_hash) & (F.col("status") == "SUCCESS"))
        .limit(1)
        .count()
    )
    if exact_success:
        return "SKIP_EXACT_DUPLICATE"
    date_exists = spark.table(DATA_TABLE).filter(F.col("business_date") == business_date).limit(1).count()
    return "REPLACE_CORRECTED_DATE" if date_exists else "APPEND_NEW_DATE"


def validate_frame(frame, required_columns, business_date):
    if frame.columns != list(required_columns):
        raise ValueError("Workbook column contract mismatch")
    invalid_dates = frame.filter(F.to_date("ORDER_CREATION_DATE") != F.lit(business_date)).count()
    missing_accessions = frame.filter(F.col("ACCESSION_NUMBER").isNull()).count()
    if invalid_dates or missing_accessions:
        raise ValueError(f"Validation failed: invalid_dates={invalid_dates}, missing_accessions={missing_accessions}")


# Production deployments should add their approved Excel reader, explicit type
# mappings, transactional replacement pattern, log schemas, exception handling,
# structured notebook exit, and success-only archive dependency here.
