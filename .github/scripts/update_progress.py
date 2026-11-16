from pathlib import Path
import re

path = Path("README.md")
text = path.read_text(encoding="utf-8")

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
    "<sub>Automatically refreshed after each checklist update.</sub>\n\n"
    "</div>\n"
    f"{end}"
)
before, remainder = text.split(start, 1)
_, after = remainder.split(end, 1)
text = before + replacement + after

# Add a compact completion count to each expandable roadmap stage.
pattern = re.compile(r"(?s)<details>\s*<summary(?: id=\"stage-(\d+)\")?>(.*?)</summary>(.*?)</details>")
def update_stage(match):
    stage_id, summary, body = match.groups()
    summary = re.sub(r"\s*<sub>\d+/\d+ complete</sub>", "", summary)
    done = len(re.findall(r"(?m)^\s*- \[x\]\s+", body, flags=re.IGNORECASE))
    todo = len(re.findall(r"(?m)^\s*- \[ \]\s+", body))
    total_stage = done + todo
    count = f" <sub>{done}/{total_stage} complete</sub>" if total_stage else ""
    return f"<details>\n<summary" + (f' id="stage-{stage_id}"' if stage_id else "") + f">{summary}{count}</summary>{body}</details>"

text = pattern.sub(update_stage, text)
path.write_text(text, encoding="utf-8")
print(f"Overall progress: {percent}% ({checked}/{total})")
