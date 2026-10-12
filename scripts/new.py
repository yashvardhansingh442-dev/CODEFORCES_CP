"""Create a solution file from the template.
Usage:
  python scripts/new.py practice 1850B ten_words_of_wisdom 800
  python scripts/new.py contest 2026/2150-div2 A
"""
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
tpl = (root / "templates" / "template.py").read_text()

mode = sys.argv[1]
if mode == "practice":
    pid, name, rating = sys.argv[2], sys.argv[3], sys.argv[4]
    out = root / "practice" / rating / f"{pid}_{name}.py"
else:
    folder, idx = sys.argv[2], sys.argv[3]
    out = root / "contests" / folder / f"{idx}.py"

out.parent.mkdir(parents=True, exist_ok=True)
if out.exists():
    sys.exit(f"{out} already exists")
out.write_text(tpl)
print(f"created {out}")
