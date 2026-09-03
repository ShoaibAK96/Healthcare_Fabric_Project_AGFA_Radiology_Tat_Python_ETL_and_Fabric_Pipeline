from openpyxl import load_workbook
from radiology_etl.excel_writer import write_workbook_atomic


def test_atomic_workbook_creation(tmp_path):
    output = tmp_path / "demo.xlsx"
    write_workbook_atomic([{"A": 1, "B": 2}], ("A", "B"), "Data", output)
    assert output.exists()
    assert not (tmp_path / "demo.xlsx.part").exists()
    book = load_workbook(output, read_only=True)
    assert list(book["Data"].values) == [("A", "B"), (1, 2)]
