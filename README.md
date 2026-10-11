# CODEFORCES_CP

My competitive programming journey on Codeforces, in Python.

- Profile: https://codeforces.com/profile/<your_handle>
- Language: Python 3 (submit with **PyPy 3** for speed)

## Stats
<!-- STATS:START -->
<!-- STATS:END -->

Update with: `python scripts/stats.py <your_handle>`

## Structure
| Folder | Purpose |
|--------|---------|
| `templates/` | Starter template with fast IO |
| `contests/<year>/<round>/` | Live contest solutions (A.py, B.py, ...) |
| `practice/<rating>/` | Problemset solves grouped by rating |
| `topics/` | Patterns and notes per topic (dp, graphs, ...) |
| `upsolve.md` | Problems I couldn't solve in contest + the idea I missed |
| `scripts/` | `new.py` (scaffold a file), `stats.py` (README stats) |

## Workflow
1. `python scripts/new.py practice 1850B ten_words_of_wisdom 800`
2. Solve, test on samples, submit (PyPy 3).
3. Commit only accepted solutions, with the key idea in the header.
4. Anything missed goes into `upsolve.md`.
