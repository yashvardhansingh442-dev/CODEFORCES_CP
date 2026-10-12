"""Regenerate the stats table in README.md from the public Codeforces API.
Usage: python scripts/stats.py <your_codeforces_handle>
Note: the API gives metadata only (no source code), so code is committed manually.
"""
import json
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

handle = sys.argv[1]
url = f"https://codeforces.com/api/user.status?handle={handle}"
with urllib.request.urlopen(url) as r:
    data = json.load(r)
if data["status"] != "OK":
    sys.exit(data.get("comment", "API error"))

solved = {}
for s in data["result"]:
    if s.get("verdict") == "OK":
        p = s["problem"]
        solved[(p["contestId"], p["index"])] = p.get("rating")

by_rating = Counter(r for r in solved.values() if r)
unrated = sum(1 for r in solved.values() if not r)

lines = ["| Rating | Solved |", "|--------|--------|"]
for r in sorted(by_rating):
    lines.append(f"| {r} | {by_rating[r]} |")
if unrated:
    lines.append(f"| unrated | {unrated} |")
lines.append(f"| **Total** | **{len(solved)}** |")
table = "\n".join(lines)

readme = Path(__file__).resolve().parent.parent / "README.md"
text = readme.read_text()
new = re.sub(
    r"(<!-- STATS:START -->).*?(<!-- STATS:END -->)",
    lambda m: f"{m.group(1)}\n{table}\n{m.group(2)}",
    text,
    flags=re.S,
)
readme.write_text(new)
print(f"Updated README: {len(solved)} problems solved")
