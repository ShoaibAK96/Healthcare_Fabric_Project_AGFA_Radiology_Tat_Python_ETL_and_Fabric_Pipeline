"""Generate public-safe architecture diagrams for the portfolio README."""

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "images"
NAVY = "#0B2239"
BLUE = "#1769A6"
CYAN = "#1CA6C8"
TEAL = "#148F8C"
GREEN = "#278E58"
AMBER = "#E59A22"
RED = "#D8524E"
INK = "#18324B"
MUTED = "#5B7288"
PAPER = "#F5F8FB"
WHITE = "#FFFFFF"
LINE = "#B9CDE0"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size: int, bold: bool = False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)


def centered(draw, box, text, size, color=INK, bold=False, spacing=8):
    x1, y1, x2, y2 = box
    lines = text.split("\n")
    f = font(size, bold)
    heights = [draw.textbbox((0, 0), line, font=f)[3] for line in lines]
    total = sum(heights) + spacing * (len(lines) - 1)
    y = y1 + (y2 - y1 - total) / 2
    for line, h in zip(lines, heights):
        width = draw.textbbox((0, 0), line, font=f)[2]
        draw.text(((x1 + x2 - width) / 2, y), line, font=f, fill=color)
        y += h + spacing


def arrow(draw, start, end, color=CYAN, width=12):
    draw.line((start, end), fill=color, width=width)
    x, y = end
    draw.polygon([(x, y), (x - 22, y - 15), (x - 22, y + 15)], fill=color)


def summary():
    img = Image.new("RGB", (2200, 1250), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 2200, 145), fill=NAVY)
    d.text((85, 35), "Radiology TAT — End-to-End Data Pipeline", font=font(43, True), fill=WHITE)
    d.text((85, 95), "Secure extraction → validated handoff → Microsoft Fabric → governed staging", font=font(24), fill="#C8D8E8")

    stages = [
        ("1  SOURCE", "Previous-day extract\nControlled schema", BLUE),
        ("2  PYTHON ETL", "Validate and publish\nAtomic workbook", TEAL),
        ("3  SECURE HANDOFF", "Managed file drop\nEnvironment-neutral", CYAN),
        ("4  FABRIC PIPELINE", "Scheduled ingestion\nGateway-mediated copy", BLUE),
        ("5  SPARK + DELTA", "Validate • hash • load\nAppend / replace / skip", GREEN),
        ("6  ARCHIVE", "Success-only archival\nIncoming area cleared", TEAL),
    ]
    left, top, w, h, gap = 75, 260, 260, 185, 72
    for i, (title, body, color) in enumerate(stages):
        x = left + i * (w + gap)
        d.rounded_rectangle((x, top, x + w, top + h), radius=22, fill=WHITE, outline=color, width=5)
        d.rectangle((x, top, x + w, top + 55), fill=color)
        centered(d, (x, top, x + w, top + 55), title, 20, WHITE, True)
        centered(d, (x + 14, top + 62, x + w - 14, top + h - 8), body, 19)
        if i < len(stages) - 1:
            arrow(d, (x + w + 10, top + h // 2), (x + w + gap - 10, top + h // 2))

    d.rounded_rectangle((75, 525, 1420, 730), radius=24, fill=WHITE, outline=LINE, width=4)
    d.text((110, 560), "VERIFIED DAILY RESULTS", font=font(27, True), fill=BLUE)
    metrics = [("Two test dates", "Validated"), ("424 rows", "Loaded"), ("Exact rerun", "0 duplicate rows")]
    for i, (a, b) in enumerate(metrics):
        x = 115 + i * 400
        d.text((x, 630), a, font=font(29, True), fill=INK)
        d.text((x, 676), b, font=font(21), fill=MUTED)

    d.rounded_rectangle((75, 790, 2125, 1070), radius=24, fill="#FFF8EB", outline=AMBER, width=4)
    d.text((110, 825), "ONE-TIME HISTORICAL PATH — VALIDATED, RETAINED IN STAGING", font=font(29, True), fill="#97610B")
    hist = [("Historical workbook", "717,646 rows\nverified source count"), ("Streamed processing", "15 batches\n1,003 business dates"), ("Audit passed", "0 duplicates\n0 validation failures"), ("STAGING ONLY", "Promotion excluded\nfrom public implementation")]
    hw, hg = 380, 95
    for i, (a, b) in enumerate(hist):
        x = 110 + i * (hw + hg)
        d.rounded_rectangle((x, 895, x + hw, 1025), radius=18, fill=WHITE, outline=AMBER, width=3)
        d.text((x + 25, 915), a, font=font(23, True), fill=INK)
        d.multiline_text((x + 25, 958), b, font=font(19), fill=MUTED, spacing=7)
        if i < len(hist) - 1:
            arrow(d, (x + hw + 12, 960), (x + hw + hg - 12, 960), AMBER, 8)

    d.text((85, 1140), "Verified end state: daily automation active; historical data remains isolated in governed staging.", font=font(28, True), fill=NAVY)
    path = OUT / "radiology-tat-pipeline_Summary.png"
    img.save(path, optimize=True)
    return path


def detailed():
    stages = [
        ("OBJECTIVE & SOURCE", ["Automate radiology turnaround-time delivery from an Oracle source.", "Refined the extract to the complete previous calendar day."], BLUE),
        ("PYTHON ETL FOUNDATION", ["Python ETL uses environment-based connection settings.", "Approved SQL is separated from code; workbook contract contains 20 columns."], TEAL),
        ("RELIABLE FILE PUBLICATION", ["Output is named from the validated business date.", "A temporary file is renamed only after workbook completion."], CYAN),
        ("AUTOMATED DAILY EXTRACTION", ["Scheduled execution retrieves one complete business day.", "Validation and execution logging occur before publication."], BLUE),
        ("FABRIC INGESTION", ["A pipeline copies matching workbooks through an approved gateway.", "Binary copy preserves workbook content and source filenames."], CYAN),
        ("NOTEBOOK VALIDATION", ["Validates filename date, schema, size, row dates, and type conversions.", "SHA-256 file and record hashes support lineage and duplicate control."], TEAL),
        ("DELTA LOADING & AUDIT", ["Business data, file-log, and error-log tables remain separate.", "Actions: append a new date, replace a correction, or skip an exact rerun."], GREEN),
        ("DAILY TEST RESULTS", ["Two test dates loaded 424 rows in total.", "An exact-file rerun added zero duplicate rows; successful files were archived."], GREEN),
        ("ISSUE RESOLUTION", ["A source-side maintenance issue was isolated from ETL defects.", "Header aliases and copy settings were aligned with the approved contract."], RED),
        ("HISTORICAL ONE-TIME LOAD", ["The historical workbook contained 717,646 rows and 20 columns.", "Read-only streaming processed 15 batches into an isolated staging table."], AMBER),
        ("HISTORICAL AUDIT", ["Audit reported 1,003 business dates and zero exact duplicates.", "Completeness, date-range, overlap, and failure checks passed."], AMBER),
        ("GOVERNANCE DECISION & FINAL STATE", ["Historical records remain in governed staging.", "Production promotion is intentionally absent from the public implementation."], NAVY),
    ]
    height = 320 + len(stages) * 285
    img = Image.new("RGB", (2400, height), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 2400, 175), fill=NAVY)
    d.text((105, 42), "Radiology TAT — Detailed Project Journey", font=font(48, True), fill=WHITE)
    d.text((105, 112), "From source extraction and Python automation to Fabric processing and governed historical staging", font=font(25), fill="#C8D8E8")
    y = 240
    for idx, (title, bullets, color) in enumerate(stages, 1):
        d.ellipse((80, y + 42, 155, y + 117), fill=color)
        centered(d, (80, y + 42, 155, y + 117), str(idx), 24, WHITE, True)
        if idx < len(stages):
            d.line((117, y + 117, 117, y + 285), fill=LINE, width=6)
        d.rounded_rectangle((200, y, 2290, y + 225), radius=22, fill=WHITE, outline=color, width=4)
        d.rectangle((200, y, 220, y + 225), fill=color)
        d.text((255, y + 28), f"{idx:02d}  {title}", font=font(27, True), fill=color)
        by = y + 84
        for bullet in bullets:
            d.ellipse((260, by + 9, 274, by + 23), fill=color)
            d.text((300, by), bullet, font=font(22), fill=INK)
            by += 56
        y += 285
    d.rectangle((0, height - 110, 2400, height), fill=NAVY)
    centered(d, (0, height - 110, 2400, height), "VERIFIED END STATE  •  DAILY AUTOMATION ACTIVE  •  HISTORICAL PROMOTION NOT INCLUDED", 26, WHITE, True)
    path = OUT / "radiology-tat-pipeline_Detailed.png"
    img.save(path, optimize=True)
    return path


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    old = [OUT / "architecture-summary.png", OUT / "architecture-detailed.png"]
    generated = [summary(), detailed()]
    for path in old:
        if path.exists():
            path.unlink()
    for path in generated:
        print(path.relative_to(ROOT))
