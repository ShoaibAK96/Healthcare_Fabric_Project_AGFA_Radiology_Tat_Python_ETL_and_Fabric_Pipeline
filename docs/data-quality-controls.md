# Data Quality and Reliability Controls

| Control | Purpose |
|---|---|
| Exact column contract | Prevent schema drift and silent column reordering |
| Filename business date | Connect each file to one processing date |
| Row-level date validation | Reject rows outside the declared date |
| Required accession | Prevent untraceable business records |
| SHA-256 file hash | Detect exact file reprocessing |
| Deterministic record hash | Support lineage and duplicate analysis |
| Corrected-date replacement | Replace a changed file for an existing date |
| Atomic `.part` publication | Prevent ingestion of incomplete workbooks |
| File and error logs | Separate operational audit from business data |
| Success-only archive dependency | Preserve failed input for investigation |
