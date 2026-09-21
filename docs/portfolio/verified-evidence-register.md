# Verified Evidence Register

| Evidence category | AGFA project evidence | Public-use treatment |
|---|---|---|
| Verified implementation | Python Oracle extraction, controlled file publication, managed Microsoft Fabric pipelines, PySpark validation, Delta business/file/error tables, hashing, corrected-date replacement, duplicate skipping and archiving | Describe generically; use reconstructed examples and environment variables |
| Verified implementation | Separate daily TAT, manual-date backfill, historical staging and addendum workloads | Safe to describe without internal infrastructure identifiers |
| Verified production outcome | Daily files were loaded, corrected dates were regenerated, and exact duplicate reruns wrote no additional business rows | Describe behavior; avoid exposing internal table or server names |
| Verified production outcome | First controlled addendum load processed one workbook and wrote two Delta rows with zero failures | Safe as an aggregate metric |
| Verified staging outcome | A high-volume, multi-year historical workbook was processed in controlled streaming batches | Exact operational volumes retained only in private records |
| Verified staging outcome | Historical audit used record-level hashes, duplicate checks, key-date validation and date reconciliation | Public-safe qualitative quality evidence |
| User-confirmed outcome | Daily and addendum Windows tasks and Fabric pipelines were scheduled independently | Show generalized times only where useful |
| User-confirmed outcome | Public and private repository packaging was requested as two distinct security boundaries | Public repository stays sanitized; private repository retains approved internal source |
| Implemented, pending production occurrence | Addendum zero-row logic logs `NO_DATA`, exits successfully and publishes no workbook | State as implemented; do not claim a later scheduled zero-row validation unless confirmed |
| Staging-only | Historical records remain in a dedicated staging Delta table | Must always be marked staging-only |
| Locked/unexecuted | Historical promotion into the daily production fact was prepared but deliberately locked and not executed | Never present as a completed load |
| Reconstructed public example | Modular Python package, SQL templates, Fabric notebook sources, pipeline descriptions and synthetic samples in the public repository | Label as public-safe reconstruction, not exact production source |
| Original private source | Available daily Python ETL variants, original SQL, command files, manual-date extractor and addendum ETL | Keep only in private repository |
| Unknown/unavailable artifact | Exact current orchestration exports, scheduler definitions and live storage DDL exports | Record as missing authoritative exports; do not recreate and label as original |
| Superseded approach | Early Oracle thin-client/connectivity attempts and the unwanted workbook column | Retain only as issue-resolution history |
| Future work | Public/private GitHub publication, profile optimization and portfolio website | Not completed by this packaging workflow |

## Evidence rules carried into all outputs

- Use the latest confirmed project state when earlier evidence conflicts.
- Preserve historical staging and production as separate states.
- Do not expose record-level healthcare data, credentials, private infrastructure or internal identities publicly.
- Do not claim business savings, performance percentages or organizational impact that was not measured.
- Do not represent reconstructed public files as exact production exports.
