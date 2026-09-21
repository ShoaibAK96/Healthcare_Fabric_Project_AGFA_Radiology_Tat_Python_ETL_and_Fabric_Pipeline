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

Schedule source extraction and platform ingestion with a sufficient completion buffer. Adapt the cadence to the approved service-level agreement without publishing production timing details.
