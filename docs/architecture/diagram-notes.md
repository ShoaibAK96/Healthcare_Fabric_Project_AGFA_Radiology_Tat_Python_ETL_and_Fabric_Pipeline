# Diagram Interpretation

## For nontechnical readers

The platform collects two related kinds of radiology information from an operational database: daily turnaround-time records and report addendums. Python prepares controlled workbooks, and Microsoft Fabric validates and stores them for analytics. Files are only archived after successful processing.

The daily path can append a new date, replace a corrected date, or skip a file already processed. The addendum path treats a day with no records as a successful `NO_DATA` outcome and avoids creating an empty workbook.

A separate high-volume, multi-year historical workbook was streamed and audited in a dedicated staging table. The dotted promotion line is intentionally marked as locked and unexecuted because the governed implementation kept that historical dataset separate from the scheduled daily production fact.

## Visual legend

- Blue: source systems and extraction
- Teal: movement, validation and orchestration
- Green: successful storage and archive outcomes
- Amber: decisions, recovery and issue resolution
- Orange: historical or staging-only work
- Dotted lines: manual, controlled or deliberately unexecuted paths

## Output dimensions

- `AGFA_Radiology_Platform_Summary.png`: 2200 × 1250 pixels
- `AGFA_Radiology_Platform_Detailed.png`: 2400 × 4190 pixels

## Rendering source

`render_diagrams.py` creates both PNGs using deterministic code-native drawing. The diagrams do not use generative imagery.
