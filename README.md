<div align="center">

# ⚔️ CODEFORCES_CP

**My competitive programming journey on Codeforces — written in Python, one problem at a time.**

[![Codeforces](https://img.shields.io/badge/Codeforces-yashvardhansingh442-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/yashvardhansingh442)
[![Language](https://img.shields.io/badge/Python-PyPy%203-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://pypy.org/)
[![Status](https://img.shields.io/badge/Status-Grinding-success?style=for-the-badge)](#-roadmap)

</div>

---

## 📖 About

This repo is my public log of competitive programming. Every accepted solution lives here with the **key idea written in its header**, and every problem I fail to solve in contest goes into [`upsolve.md`](upsolve.md) along with the idea I missed.

The goal isn't just a rating number. It's building the problem-solving speed and pattern recognition that carry over into everything else I build (algorithms, systems, robotics/AI work).

Companion repo: [LEETCODE_DSA](https://github.com/yashvardhansingh442-dev/LEETCODE_DSA) — structured DSA practice that feeds into this one.

## 📊 Stats

<!-- STATS:START -->
<!-- STATS:END -->

> Auto-updated with `python scripts/stats.py yashvardhansingh442`

| | |
|---|---|
| **Handle** | [yashvardhansingh442](https://codeforces.com/profile/yashvardhansingh442) |
| **Current rating** | Unrated (just getting started) |
| **Language** | Python 3 — submitted with **PyPy 3** |
| **Started** | October 2026 |

## 🗂️ Repository Structure

```
CODEFORCES_CP/
├── templates/          # Starter template with fast IO
├── contests/
│   └── <year>/<round>/ # Live contest solutions (A.py, B.py, ...)
├── practice/
│   └── <rating>/       # Problemset solves grouped by difficulty rating
├── topics/             # Patterns & notes per topic (dp, graphs, ...)
├── scripts/
│   ├── new.py          # Scaffold a new solution file
│   └── stats.py        # Refresh the README stats
├── upsolve.md          # Contest misses + the idea I didn't see
└── README.md
```

| Folder | Purpose |
|--------|---------|
| `templates/` | Starter template with fast input/output |
| `contests/<year>/<round>/` | Solutions written during live rounds |
| `practice/<rating>/` | Problemset solves, bucketed by rating (800, 900, 1000, ...) |
| `topics/` | Reusable patterns and notes: DP, graphs, greedy, math, binary search... |
| `upsolve.md` | Problems I couldn't finish in contest, with the missed insight |
| `scripts/` | Small tools to scaffold files and update stats |

## ⚡ Workflow

1. **Scaffold** a solution file:
   ```bash
   python scripts/new.py practice 1850B ten_words_of_wisdom 800
   ```
2. **Solve** it and test against the samples.
3. **Submit** on Codeforces using **PyPy 3** (much faster than CPython).
4. **Commit only accepted solutions**, with the key idea in the file header.
5. **Log misses** in [`upsolve.md`](upsolve.md) and revisit them later.

## 🧩 Solution File Format

Every solution starts with a short header so it's useful months later:

```python
"""
Problem : 1850B - Ten Words of Wisdom
Rating  : 800
Tags    : implementation, sortings
Idea    : Filter by a_i <= 10, then pick the one with max b_i.
Verdict : Accepted (PyPy 3)
"""
import sys
input = sys.stdin.readline

def solve():
    ...

for _ in range(int(input())):
    solve()
```

## 🛠️ Template

A minimal fast-IO template lives in [`templates/`](templates/):

```python
import sys
input = sys.stdin.readline

def ints():
    return list(map(int, input().split()))

def solve():
    pass

def main():
    t = int(input())
    for _ in range(t):
        solve()

main()
```

## 🧠 Topics Tracker

| Topic | Status | Notes |
|-------|--------|-------|
| Implementation / Brute force | 🟡 Starting | |
| Math / Number theory | ⚪ Not started | |
| Greedy | ⚪ Not started | |
| Sorting & Binary search | ⚪ Not started | |
| Prefix sums / Two pointers | ⚪ Not started | |
| Constructive algorithms | ⚪ Not started | |
| Graphs (BFS / DFS / DSU) | ⚪ Not started | |
| Dynamic programming | ⚪ Not started | |
| Data structures (heaps, segment tree) | ⚪ Not started | |

## 🎯 Roadmap

- [ ] Complete the first rated contest and get an initial rating
- [ ] Solve 100 problems rated 800–1000
- [ ] Reach **Pupil** (1200+)
- [ ] Reach **Specialist** (1400+)
- [ ] Reach **Expert** (1600+)
- [ ] Write up notes for every core topic in `topics/`

## 📝 Principles

- **Upsolve everything.** A failed problem is only wasted if I don't learn the missing idea.
- **Idea first, code second.** Every commit explains *why* the solution works.
- **Consistency over intensity.** A little every day beats a weekend binge.
- **Read editorials only after a real attempt.**

## 🔗 Links

- Codeforces: [yashvardhansingh442](https://codeforces.com/profile/yashvardhansingh442)
- LeetCode: [Yash04_09](https://leetcode.com/u/Yash04_09/)
- GitHub: [yashvardhansingh442-dev](https://github.com/yashvardhansingh442-dev)

---

<div align="center">

*Solve. Fail. Upsolve. Repeat.*

</div>
