from pathlib import Path
import re

readme_path = Path("README.md")
text = readme_path.read_text(encoding="utf-8")

start = "<!-- PROGRESS:START -->"
end = "<!-- PROGRESS:END -->"
if start not in text or end not in text:
    raise SystemExit("Progress markers are missing from README.md")

roadmap_start = text.index("## 🗺️ Learning roadmap")
roadmap_end = text.index("---", roadmap_start)
roadmap = text[roadmap_start:roadmap_end]

checked = len(re.findall(r"(?m)^\s*- \[x\]\s+", roadmap, flags=re.IGNORECASE))
unchecked = len(re.findall(r"(?m)^\s*- \[ \]\s+", roadmap))
total = checked + unchecked
percent = round((checked / total) * 100) if total else 0

filled = round(percent / 5)
bar = "🟩" * filled + "⬜" * (20 - filled)

replacement = (
    f"{start}\n"
    "<div align=\"center\">\n\n"
    f"# {percent}%\n\n"
    f"**{checked} of {total} learning tasks completed**\n\n"
    f"{bar}\n\n"
    "<sub>Progress updates automatically when I commit changes to this checklist.</sub>\n\n"
    "</div>\n"
    f"{end}"
)

before, remainder = text.split(start, 1)
_, after = remainder.split(end, 1)
readme_path.write_text(before + replacement + after, encoding="utf-8")
print(f"Updated learning progress: {percent}% ({checked}/{total})")
