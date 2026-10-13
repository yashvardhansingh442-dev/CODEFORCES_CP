# 158A - Next Round

**Platform:** Codeforces
**Problem:** [158A](https://codeforces.com/problemset/problem/158/A)
**Difficulty:** 800
**Tags:** implementation
**Language:** Python 3
**Status:** Accepted

## Problem

`n` participants finished a contest, and their scores are given in non-increasing order. A participant advances to the next round if both conditions hold:

1. Their score is **at least** the score of the participant in `k`-th place.
2. Their score is **positive**.

Print how many participants advance.

**Input:**
- Line 1: two integers `n` and `k` (`1 ≤ k ≤ n ≤ 50`)
- Line 2: `n` integers `a1 ≥ a2 ≥ ... ≥ an` (`0 ≤ ai ≤ 100`)

**Output:** one integer, the number of participants who advance

### Examples

| Input | Output |
|-------|--------|
| `8 5`<br>`10 9 8 7 7 7 5 5` | `6` |
| `4 2`<br>`0 0 0 0` | `0` |

## Approach

Because the scores are already sorted, the k-th place score is simply `a[k-1]` (0-indexed). That is the cutoff.

Count every score that satisfies both rules:

- `score >= a[k-1]`, so ties with the k-th place also advance, which is why the first example gives 6 rather than 5.
- `score > 0`, because a score of 0 never advances even if it equals the cutoff, which is why the second example gives 0.

## Solution

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))

threshold = a[k - 1]
count = 0
for x in a:
    if x >= threshold and x > 0:
        count += 1

print(count)
```

## Complexity

- **Time:** O(n)
- **Space:** O(n) for the input list

## Edge Cases

- The k-th place score is 0, so nobody with 0 advances.
- Several participants tie with the k-th place, so more than `k` people can advance.
- `k = n`: the cutoff is the lowest score, so everyone with a positive score advances.

## Key Takeaway

When the data is already sorted, the cutoff comes from a direct index lookup, so no sorting is needed. Also check whether ties and zero values change the count.
