from datetime import date
from pathlib import Path
from typing import Iterator, Mapping, Any
import os


def extract_rows(sql_file: str | Path, business_date: date) -> Iterator[Mapping[str, Any]]:
    try:
        import oracledb
    except ImportError as exc:
        raise RuntimeError("Install the optional Oracle dependency") from exc

    dsn = oracledb.makedsn(
        os.environ["ORACLE_HOST"],
        int(os.getenv("ORACLE_PORT", "1521")),
        service_name=os.environ["ORACLE_SERVICE_NAME"],
    )
    sql = Path(sql_file).read_text(encoding="utf-8")
    with oracledb.connect(
        user=os.environ["ORACLE_USERNAME"],
        password=os.environ["ORACLE_PASSWORD"],
        dsn=dsn,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, business_date=business_date)
            columns = tuple(item[0] for item in cursor.description)
            for values in cursor:
                yield dict(zip(columns, values))
