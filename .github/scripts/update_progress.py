from pathlib import Path
import re

readme_path = Path("README.md")
text = readme_path.read_text(encoding="utf-8")

start = "<!-- PROGRESS:START -->"
end = "<!-- PROGRESS:END -->"
if start not in text or end not in text:
    raise SystemExit("Progress markers are missing from README.md")

# Count only checklist tasks in the roadmap, not examples or instructions elsewhere.
roadmap_start = text.index("## 🧭 Learning roadmap & checklist")
roadmap_end = text.index("## 📁 Current repository work")
roadmap = text[roadmap_start:roadmap_end]

checked = len(re.findall(r"(?m)^\s*- \[x\]\s+", roadmap, flags=re.IGNORECASE))
unchecked = len(re.findall(r"(?m)^\s*- \[ \]\s+", roadmap))
total = checked + unchecked
percent = round((checked / total) * 100) if total else 0

replacement = (
    f"{start}\n"
    f"**Overall completion: {percent}% ({checked} / {total} topics)**\n\n"
    "Progress is calculated automatically from the checklist below. "
    "Only tick a topic when you can explain it and complete a small exercise without copying.\n"
    f"{end}"
)

before, remainder = text.split(start, 1)
_, after = remainder.split(end, 1)
readme_path.write_text(before + replacement + after, encoding="utf-8")
print(f"Updated learning progress: {percent}% ({checked}/{total})")
