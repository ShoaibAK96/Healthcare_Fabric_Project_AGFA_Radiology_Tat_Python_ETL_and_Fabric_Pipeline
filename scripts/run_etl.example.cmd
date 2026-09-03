@echo off
setlocal
call .venv\Scripts\activate.bat
python -m radiology_etl.cli --config config\config.example.yaml
exit /b %ERRORLEVEL%
