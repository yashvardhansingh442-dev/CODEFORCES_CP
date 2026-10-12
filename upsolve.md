# Upsolve log

Problems where my first idea was wrong, I got stuck, or I needed help. Clean solves live in `practice/`, not here.

**Outcome key:** `alone` = solved myself (but the first idea needed fixing) · `hint` = needed a nudge · `editorial` = read the solution · `late` = solved after the contest ended · `retry` = failed the one-week re-attempt

| Date | Problem | Rating | Tags | Outcome | What I missed | Fix / idea | Re-attempt |
|------|---------|--------|------|---------|---------------|------------|------------|
| 2026-10-11 | [4A - Watermelon](https://codeforces.com/problemset/problem/4/A) | 800 | math, brute force | alone | First thought: any even `w` works. Forgot `w = 2` fails, since both parts must be positive and even (1 + 1 is odd) | Answer is YES only if `w > 2` and `w % 2 == 0` | 2026-10-18 |
| 2026-10-11 | [71A - Way Too Long Words](https://codeforces.com/problemset/problem/71/A) | 800 | strings, implementation | editorial | Needed a tutorial to get started (edit: what exactly was unclear?) | If `len(word) > 10`: `word[0] + str(len(word) - 2) + word[-1]`, else print as is | 2026-10-18 |

## Recurring weak spots

Update this every ~10 rows by scanning the "What I missed" column.

- Edge cases at the smallest inputs (4A: `w = 2`). Check minimum values before submitting.
- Getting started on string problems without a tutorial (71A). Practice slicing and indexing (`s[0]`, `s[-1]`, `len(s)`).

## Habits

- Upsolve within 1-2 days of the contest.
- Re-attempt a week later without looking at notes. If it fails, mark `retry` instead of closing the row.
- Keep table cells to one line. Longer write-ups go in `practice/` or `topics/` and get linked here.
