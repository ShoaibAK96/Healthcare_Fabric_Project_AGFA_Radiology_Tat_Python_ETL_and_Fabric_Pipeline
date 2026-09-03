from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", ".gitignore", ".env.example", "pyproject.toml",
    "src/radiology_etl/cli.py", "fabric/notebooks/daily_transformation.py",
    "docs/public-release-checklist.md", "sample_data/radiology_tat_sample.csv",
]
PATTERNS = {
    "private IPv4": re.compile(r"\b(?:10\.|192\.168\.|172\.(?:1[6-9]|2\d|3[01])\.)"),
    "Windows network share": re.compile(r"\\\\[A-Za-z0-9_.-]+\\"),
    "possible secret assignment": re.compile(r"(?i)(password|token|secret)\s*[=:]\s*['\"][^$<{][^'\"]{5,}['\"]"),
}


def main() -> int:
    failures = [f"Missing required file: {name}" for name in REQUIRED if not (ROOT / name).exists()]
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix in {".png", ".zip"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                failures.append(f"{label} found in {path.relative_to(ROOT)}")
    if failures:
        print("\n".join(failures))
        return 1
    print("Repository validation passed: structure complete and no blocked patterns found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
