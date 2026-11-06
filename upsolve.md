# Upsolve log

Problems where my first idea was wrong, I got stuck, or I needed help. Clean solves live in `practice/`, not here.

**Outcome key:** `alone` = solved myself (but the first idea needed fixing) · `hint` = needed a nudge · `editorial` = read the solution · `late` = solved after the contest ended · `retry` = failed the one-week re-attempt

| Date | Problem | Rating | Tags | Outcome | What I missed | Fix / idea | Re-attempt |
|------|---------|--------|------|---------|---------------|------------|------------|
| 2026-10-11 | [4A - Watermelon](https://codeforces.com/problemset/problem/4/A) | 800 | math, brute force | alone | First thought: any even `w` works. Forgot `w = 2` fails, since both parts must be positive and even (1 + 1 is odd) | Answer is YES only if `w > 2` and `w % 2 == 0` | NA |
| 2026-10-11 | [71A - Way Too Long Words](https://codeforces.com/problemset/problem/71/A) | 800 | strings, implementation | editorial | Needed a tutorial to get started (edit: what exactly was unclear?) | If `len(word) > 10`: `word[0] + str(len(word) - 2) + word[-1]`, else print as is | NA |
| 2026-10-12 | [231A - Team](https://codeforces.com/problemset/problem/231/A) | 800 | greedy, brute force, implementation | alone | (edit: anything you missed or got stuck on?) | For each problem, read the 3 values and count it if their sum is >= 2 | NA |
| 2026-10-13 | [50A - Domino piling](https://codeforces.com/problemset/problem/50/A) | 800 | math, greedy | alone | (edit: anything you missed or got stuck on?) | Each domino covers 2 cells, so the answer is `(M * N) // 2` | 2026-10-20 |
| 2026-10-13 | [158A - Next Round](https://codeforces.com/problemset/problem/158/A) | 800 | implementation | alone | (edit: anything you missed or got stuck on?) | Count scores `>= a[k-1]` and `> 0` (a zero score never advances) | 2026-10-20 |
| 2026-10-14 | [236A - Boy or Girl](https://codeforces.com/problemset/problem/236/A) | 800 | brute force, implementation, strings | alone | Compilation error on the first submit (edit: what was the error?) | Count distinct characters with `len(set(s))`: even → `CHAT WITH HER!`, odd → `IGNORE HIM!` | NA |
| 2026-10-16 | [339A - Helpful Maths](https://codeforces.com/problemset/problem/339/A) | 800 | implementation, sortings, strings | alone | (edit: anything you missed or got stuck on?) | `s.split('+')`, sort the numbers, join back with `'+'` | 2026-10-23 |
| 2026-10-17 | [112A - Petya and Strings](https://codeforces.com/problemset/problem/112/A) | 800 | implementation, strings | alone | (edit: anything you missed or got stuck on?) | Lowercase both strings, compare, print -1 / 0 / 1 | NA |
| 2026-10-18 | [266A - Stones on the Table](https://codeforces.com/problemset/problem/266/A) | 800 | implementation | alone | (edit: anything you missed or got stuck on?) | Count adjacent equal pairs `s[i] == s[i+1]` | NA |
| 2026-10-21 | [266B - Queue at the School](https://codeforces.com/problemset/problem/266/B) | 800 | implementation, constructive algorithms | alone | (edit: anything you missed or got stuck on?) | Simulate `t` seconds, swapping each `BG` to `GB` in one left-to-right pass (skip past a swapped pair so a boy moves only once per second) | NA |
| 2026-10-27 | [110A - Nearly Lucky Number](https://codeforces.com/problemset/problem/110/A) | 800 | implementation | alone | (edit: anything you missed or got stuck on?) | Count the digits `4` and `7`; print YES if that count is 4 or 7 | 2026-11-03 |

## Recurring weak spots

Update this every ~10 rows by scanning the "What I missed" column.

- Edge cases at the smallest inputs (4A: `w = 2`). Check minimum values before submitting.
- Getting started on string problems without a tutorial (71A). Practice slicing and indexing (`s[0]`, `s[-1]`, `len(s)`).

## Habits

- Upsolve within 1-2 days of the contest.
- Re-attempt a week later without looking at notes. If it fails, mark `retry` instead of closing the row.
- Keep table cells to one line. Longer write-ups go in `practice/` or `topics/` and get linked here.
