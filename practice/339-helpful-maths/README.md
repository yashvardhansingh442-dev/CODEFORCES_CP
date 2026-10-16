---
TITLE: "Codeforces 339A - Helpful Maths"
PLATFORM: Codeforces
PROBLEM: 339A
DIFFICULTY: 800
TAGS: [codeforces, strings, sortings, implementation]
STATUS: solved
---

# 339A - Helpful Maths

**Link:** https://codeforces.com/problemset/problem/339/A

## Problem
Xenia is learning addition. She can only calculate a sum if the numbers are in non-decreasing order. Given a sum made only of the numbers 1, 2 and 3 (e.g. `3+2+1`), rearrange the terms so they are in non-decreasing order and print the new sum.

## Input
A non-empty string `s` with no spaces: a valid sum of the numbers 1, 2 and 3, separated by `+`. Length is at most 100.

## Output
The rearranged sum in non-decreasing order.

## Examples
| Input | Output |
|-------|--------|
| `3+2+1` | `1+2+3` |
| `1+1+3+1+3` | `1+1+1+3+3` |
| `2` | `2` |

## Approach
1. Split the string on `+`.
2. Sort the resulting tokens (single digits, so string sort equals numeric sort).
3. Join back with `+`.

## Solution (Python)
```python
s = input().split('+')
s.sort()
print('+'.join(s))
```

## Solution (C++)
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    vector<char> v;
    for (char c : s)
        if (c != '+') v.push_back(c);
    sort(v.begin(), v.end());
    for (size_t i = 0; i < v.size(); i++) {
        if (i) cout << '+';
        cout << v[i];
    }
    cout << endl;
}
```

## Complexity
- Time: O(n log n), with n at most 100
- Space: O(n)

## Edge Cases
- Single number (no `+`): print as is.
- All terms equal: output is unchanged.

## Notes
- Counting sort over {1, 2, 3} would also work in O(n).
