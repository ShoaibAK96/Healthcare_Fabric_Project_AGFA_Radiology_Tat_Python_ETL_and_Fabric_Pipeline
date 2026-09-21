# Short LinkedIn Project Post

I recently completed an end-to-end radiology data engineering platform that automates secure Oracle extraction, validated Excel publication and governed ingestion into Microsoft Fabric.

The solution separates daily turnaround-time data, operator-controlled backfills, historical staging and report addendums while supporting schema validation, SHA-256 lineage, corrected-date replacement, duplicate-safe loading, structured audit/error logs and success-only archiving.

A high-volume, multi-year historical workbook was streamed in controlled batches and passed record-hash, duplicate and date-alignment validation. In line with the governance decision, those records remain in validated staging rather than the daily production fact.

This project reinforced an important engineering principle: a reliable pipeline must explicitly handle corrected inputs, duplicate reruns, recovery workflows, empty business days and archival safety—not only successful loads.

#DataEngineering #MicrosoftFabric #Python #PySpark #DeltaLake #Oracle #HealthcareAnalytics #ETL
