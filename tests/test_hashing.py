from radiology_etl.hashing import sha256_record


def test_record_hash_is_deterministic():
    columns = ("A", "B")
    assert sha256_record({"A": "x", "B": 1}, columns) == sha256_record({"A": "x", "B": 1}, columns)


def test_column_order_affects_contract_hash():
    row = {"A": "x", "B": "y"}
    assert sha256_record(row, ("A", "B")) != sha256_record(row, ("B", "A"))
