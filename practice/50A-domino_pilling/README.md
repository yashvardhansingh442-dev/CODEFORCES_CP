# 50A - Domino Piling

**Platform:** Codeforces
**Problem:** [50A](https://codeforces.com/problemset/problem/50/A)
**Difficulty:** 800
**Tags:** greedy, math
**Language:** Python 3
**Status:** Accepted

## Problem

You have an `M × N` board and an unlimited supply of `2 × 1` dominoes. Place as many as you can so that:

1. Each domino covers exactly two cells.
2. Dominoes do not overlap.
3. Every domino lies fully inside the board.
4. Dominoes may be rotated.

Print the maximum number of dominoes that fit.

**Input:** two integers `M` and `N` (`1 ≤ M ≤ N ≤ 16`)
**Output:** one integer, the maximum number of dominoes

### Example

| Input | Output |
|-------|--------|
| `2 4` | `4`    |
| `3 3` | `4`    |

## Approach

The board has `M × N` cells and each domino covers 2 of them, so the answer can't exceed `(M × N) // 2`.

That bound is always reachable:

- If `M` or `N` is even, the board tiles perfectly with no cell left over.
- If both are odd, fill every row in pairs of columns, then fill the leftover column in pairs of rows. Exactly one cell remains empty, which is the floor in `// 2`.

So the answer is `M * N // 2`.

## Solution

```python
m, n = map(int, input().split())
print(m * n // 2)
```

## Complexity

- **Time:** O(1)
- **Space:** O(1)

## Key Takeaway

When a problem asks for the maximum number of fixed-size pieces, check the area bound first. If a constructive tiling meets that bound, the answer is a one-line formula and no DP or simulation is needed.
