# Architecture

The daily workflow deliberately separates extraction, file transfer, transformation, and storage responsibilities.

1. A read-only Oracle query extracts the complete previous calendar day.
2. Python validates the column contract and business date.
3. A write-only Excel workbook is created and atomically published.
4. A Fabric pipeline copies the workbook through an on-premises gateway.
5. A PySpark notebook validates, hashes, transforms, and chooses a load action.
6. Delta tables store business data, file-level audit records, and error details.
7. Successful files are archived; failures remain available for investigation.

The historical workflow is isolated from daily operations. Its public example stops after audited staging and deliberately contains no production-promotion code.
