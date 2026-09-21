# LinkedIn Project Post

I recently completed an end-to-end healthcare data engineering solution that automates radiology turnaround-time and report-addendum ingestion from an on-premises Oracle platform into Microsoft Fabric.

The project moved beyond simple file transfer. I designed separate operational paths for daily ingestion, controlled historical backfills, one-time historical staging, and addendum processing—each with its own validation, audit, recovery, and archive behavior.

Key engineering outcomes included:

- Secure Python extraction using Oracle connectivity and protected credential storage
- Controlled Excel generation with atomic publication, schema enforcement, row-count checks, and SHA-256 hashing
- Microsoft Fabric pipelines using an on-premises gateway, Lakehouse storage, PySpark notebooks, and Delta tables
- Idempotent load behavior for new dates, corrected dates, and exact duplicate files
- Structured business-data, file-audit, and error-log tables
- Automated archiving across source and cloud environments
- Manual-date backfill tooling for operational recovery
- A separate addendum pipeline with safe handling for legitimate zero-record days
- Streaming validation of a high-volume, multi-year historical dataset without loading the complete workbook into memory

The historical dataset passed its staging audit through record-level hashing, duplicate detection, key-date validation and business-date reconciliation. In accordance with the governance decision, it remains isolated in validated staging rather than being promoted into the scheduled daily production table.

The most valuable lesson was that dependable pipelines are defined as much by their edge cases as by their successful loads: corrected files, duplicate reruns, empty business days, schema drift, archive safety, and recoverable backfills all need explicit designs.

#DataEngineering #MicrosoftFabric #Python #PySpark #DeltaLake #Oracle #ETL #HealthcareAnalytics
