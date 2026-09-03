# Fabric Pipeline Design

```text
Copy_OnPrem_To_Fabric_Incoming
              ↓ success
Run_Radiology_TAT_Transformation
              ↓ success
Archive_Fabric_Incoming
              ↓ success
Archive_OnPrem_Incoming
```

## Required behavior

- Source wildcard: `Radiology_TAT_*.xlsx`
- Binary transfer with source filename preservation
- Transformation notebook runs only after the inbound copy succeeds
- Archive activities run only after notebook success
- “Delete files after completion” is enabled only on archive/move activities
- An empty source is treated as a successful no-file run

Recommended example timing: source ETL at 05:00 local time and Fabric ingestion at 09:00 local time. Adapt these values to the actual service-level agreement.
