from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

ROOT = Path(__file__).resolve().parent
NAVY = "#12344D"
BLUE = "#20639B"
TEAL = "#1B7F69"
GREEN = "#2F855A"
AMBER = "#B7791F"
ORANGE = "#C05621"
BG = "#F6F8FB"
WHITE = "#FFFFFF"
MUTED = "#526474"
LINE = "#B8C4CF"

def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)

def wrapped(draw, xy, text, width_chars, fnt, fill=NAVY, spacing=8):
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=width_chars) or [""])
    draw.multiline_text(xy, "\n".join(lines), font=fnt, fill=fill, spacing=spacing)

def rounded(draw, box, fill, outline=LINE, radius=24, width=3):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def arrow(draw, start, end, color=BLUE, width=6):
    draw.line([start, end], fill=color, width=width)
    x, y = end
    draw.polygon([(x, y), (x-18, y-10), (x-18, y+10)], fill=color)

def summary():
    img = Image.new("RGB", (2200, 1250), BG)
    d = ImageDraw.Draw(img)
    d.text((90, 55), "AGFA Radiology Data Platform", font=font(58, True), fill=NAVY)
    d.text((92, 130), "Daily TAT, addendum, recovery and governed historical staging", font=font(28), fill=MUTED)

    stages = [
        ("1", "Oracle Source", "Approved queries\nDaily + addendum", "#E8F1FB"),
        ("2", "Secure Python ETL", "External secret retrieval\nAtomic file publish", "#E8F1FB"),
        ("3", "Managed Transfer", "Separated processing\nareas", "#E9F7F2"),
        ("4", "Fabric Validation", "Schema, date, rows,\nfile + record hashes", "#E9F7F2"),
        ("5", "Controlled Delta", "Append / replace / skip\nAudit + error logs", "#DDF4E4"),
        ("6", "Archive", "Success-only movement\nand safe cleanup", "#DDF4E4"),
    ]
    x0, y, w, h, gap = 85, 250, 310, 265, 40
    for i, (num, title, body, color) in enumerate(stages):
        x = x0 + i*(w+gap)
        rounded(d, (x, y, x+w, y+h), color, BLUE if i < 2 else TEAL if i < 4 else GREEN)
        d.ellipse((x+20, y+20, x+74, y+74), fill=NAVY)
        d.text((x+38, y+28), num, font=font(25, True), fill=WHITE, anchor="mm")
        d.text((x+24, y+95), title, font=font(29, True), fill=NAVY)
        wrapped(d, (x+24, y+145), body, 22, font(23), fill=MUTED, spacing=8)
        if i < len(stages)-1:
            arrow(d, (x+w+7, y+h//2), (x+w+gap-8, y+h//2))

    rounded(d, (85, 585, 1035, 890), "#FFF4D6", AMBER)
    d.text((120, 620), "Operational branches", font=font(34, True), fill=NAVY)
    wrapped(d, (120, 685),
            "• Daily TAT follows a scheduled source-to-platform sequence\n"
            "• Addendum processing runs independently to isolate failures\n"
            "• Zero addendum rows: NO_DATA success; no workbook\n"
            "• Manual-date backfill: operator-controlled corrected files",
            61, font(25), fill=NAVY, spacing=12)

    rounded(d, (1085, 585, 2115, 890), "#FFF0E6", ORANGE)
    d.text((1120, 620), "Historical branch — staging only", font=font(34, True), fill=NAVY)
    wrapped(d, (1120, 685),
            "High-volume multi-year source • controlled streaming batches\n"
            "Record-level hashes • duplicate and date reconciliation\n"
            "Validated in a dedicated Delta staging table\n"
            "Production promotion was locked and not executed",
            60, font(25), fill=NAVY, spacing=12)

    rounded(d, (85, 955, 2115, 1165), WHITE, NAVY)
    d.text((120, 988), "Verified outcome", font=font(32, True), fill=GREEN)
    wrapped(d, (120, 1040),
            "Independent, scheduled and auditable daily TAT and addendum pipelines with corrected-date recovery, duplicate-safe loading, structured logs and two-stage archiving. Public portfolio uses synthetic data; original operational assets remain private.",
            130, font(26), fill=NAVY, spacing=10)
    img.save(ROOT / "AGFA_Radiology_Platform_Summary.png")

def detailed():
    stages = [
        ("1", "Objective and architecture", BLUE, ["Automate Oracle radiology TAT delivery into Microsoft Fabric.", "Separate daily, manual recovery, historical and addendum workloads.", "Keep operational and governance boundaries explicit."]),
        ("2", "Secure Oracle extraction", BLUE, ["Python with oracledb and openpyxl.", "Runtime secret retrieval keeps credentials out of source code.", "Approved query logic is retained while controlled columns are projected in Python."]),
        ("3", "Reliable workbook publication", TEAL, ["Previous-day business-date extraction.", "Header, worksheet, row-count and timestamp controls.", "Temporary workspace, SHA-256 hashing and atomic .part publication."]),
        ("4", "Daily Fabric pipeline", TEAL, ["A managed transfer delivers approved files into the Lakehouse.", "PySpark checks filename, schema, dates, numeric values and hashes.", "Decides APPEND_NEW_DATE, REPLACE_CORRECTED_DATE or SKIP_EXACT_DUPLICATE."]),
        ("5", "Count discrepancy recovery", AMBER, ["Compared source results with platform counts by business date.", "Found and removed an unintended non-reporting workbook field in Python.", "Created a manual-date utility and regenerated affected dates without changing scheduled SQL."]),
        ("6", "Historical one-time staging", ORANGE, ["Streamed a high-volume multi-year workbook in controlled batches.", "Validated record hashes, duplicates, key dates and date alignment.", "Retained in dedicated Delta staging; production promotion locked and unexecuted."]),
        ("7", "Addendum pipeline", BLUE, ["Preserved required query aliases and applied the approved business-date filter.", "Excluded a non-reporting identifier and created separate processing, storage and logging paths.", "A controlled run validated the complete path without failures."]),
        ("8", "Empty-day hardening", AMBER, ["Header-only workbooks caused Fabric validation failures on zero-record days.", "Source ETL now logs NO_DATA, exits 0 and publishes no workbook.", "Fabric NO_FILES handling then completes without writing Delta data."]),
        ("9", "Scheduling and operations", TEAL, ["Source and platform workloads use staggered daily schedules.", "Daily and addendum processing remain independent.", "Success-only archive dependencies perform cleanup after safe completion."]),
        ("10", "Current governed state", GREEN, ["Daily TAT and addendum run as independent audited workflows.", "Manual backfill remains operator controlled.", "Historical data remains staging-only; public artifacts use synthetic data."]),
    ]
    W, top, card_h, gap = 2400, 230, 330, 38
    H = top + len(stages)*(card_h+gap) + 280
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((120, 55), "AGFA Radiology Platform — Detailed Engineering Journey", font=font(56, True), fill=NAVY)
    d.text((122, 130), "Verified chronology from Oracle extraction to governed Fabric operations", font=font(29), fill=MUTED)
    cx = 210
    d.line((cx, top+35, cx, H-300), fill=LINE, width=10)
    for idx, (num, title, color, bullets) in enumerate(stages):
        y = top + idx*(card_h+gap)
        d.ellipse((cx-45, y+80, cx+45, y+170), fill=color, outline=WHITE, width=5)
        d.text((cx, y+125), num, font=font(31, True), fill=WHITE, anchor="mm")
        rounded(d, (320, y, 2280, y+card_h), WHITE, color, radius=30, width=5)
        d.rectangle((320, y, 345, y+card_h), fill=color)
        d.text((390, y+35), title, font=font(37, True), fill=NAVY)
        yy = y+105
        for bullet in bullets:
            d.ellipse((398, yy+10, 414, yy+26), fill=color)
            wrapped(d, (440, yy), bullet, 105, font(26), fill=MUTED, spacing=8)
            yy += 66
    y = H-230
    rounded(d, (120, y, 2280, H-65), "#DDF4E4", GREEN, radius=30, width=5)
    d.text((165, y+30), "VERIFIED END STATE", font=font(32, True), fill=GREEN)
    wrapped(d, (165, y+82), "Auditable daily TAT and addendum pipelines are operational; corrected-date recovery is controlled; historical data remains validated staging only; zero-row addendum handling is implemented for the next production occurrence.", 135, font(27), fill=NAVY, spacing=8)
    img.save(ROOT / "AGFA_Radiology_Platform_Detailed.png")

if __name__ == "__main__":
    summary()
    detailed()
