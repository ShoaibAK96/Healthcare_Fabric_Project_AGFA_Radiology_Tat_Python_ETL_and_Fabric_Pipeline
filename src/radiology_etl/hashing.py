import hashlib
from pathlib import Path
from typing import Mapping, Any


def sha256_file(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_record(row: Mapping[str, Any], columns: tuple[str, ...]) -> str:
    canonical = "\x1f".join("" if row.get(c) is None else str(row.get(c)).strip() for c in columns)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
