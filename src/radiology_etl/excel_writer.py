from pathlib import Path
from typing import Iterable, Mapping, Any
from openpyxl import Workbook


def write_workbook_atomic(
    rows: Iterable[Mapping[str, Any]],
    columns: tuple[str, ...],
    worksheet_name: str,
    final_path: str | Path,
) -> Path:
    final = Path(final_path)
    final.parent.mkdir(parents=True, exist_ok=True)
    temporary = final.with_suffix(final.suffix + ".part")
    workbook = Workbook(write_only=True)
    sheet = workbook.create_sheet(worksheet_name)
    sheet.append(list(columns))
    for row in rows:
        sheet.append([row.get(column) for column in columns])
    workbook.save(temporary)
    temporary.replace(final)
    return final
