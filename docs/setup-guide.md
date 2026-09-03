# Setup Guide

## Python ETL

1. Install Python 3.9 or newer and create a virtual environment.
2. Install `requirements.txt`; configure the Oracle client if Thick mode is required.
3. Copy `.env.example` to `.env` locally and provide environment-specific values.
4. Review the approved reporting view and 20-column contract.
5. Run the synthetic CSV test before enabling Oracle connectivity.
6. Configure the operating-system scheduler only after an unattended manual run succeeds.

## Microsoft Fabric

1. Create Incoming, Archive, Exceptions, Config, Historical_Incoming, and Historical_Archive folders.
2. Create or approve an on-premises gateway connection.
3. Recreate the activities documented in `fabric/pipelines/pipeline-design.md`.
4. Attach the target Lakehouse to the notebook.
5. Replace the example schema/table configuration with approved deployment values.
6. Test new-date, corrected-date, exact-duplicate, failure, and no-file scenarios.
7. Enable the schedule only after archive dependencies and notifications are verified.
