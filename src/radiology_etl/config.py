from dataclasses import dataclass
from pathlib import Path
import os
import yaml


@dataclass(frozen=True)
class Settings:
    worksheet_name: str
    filename_prefix: str
    required_columns: tuple[str, ...]
    output_directory: Path
    log_directory: Path
    sql_file: Path


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Required environment variable is not set: {name}")
    return value


def load_settings(path: str | Path) -> Settings:
    config_path = Path(path)
    raw = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    return Settings(
        worksheet_name=raw["project"]["worksheet_name"],
        filename_prefix=raw["project"]["filename_prefix"],
        required_columns=tuple(raw["validation"]["required_columns"]),
        output_directory=Path(_required_env(raw["output"]["directory_env"])),
        log_directory=Path(os.getenv(raw["output"]["log_directory_env"], "./logs")),
        sql_file=Path(raw["source"]["sql_file"]),
    )
