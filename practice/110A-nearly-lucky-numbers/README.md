# 110A - Nearly Lucky Number

**Platform:** Codeforces
**Difficulty:** 800
**Tags:** implementation
**Link:** https://codeforces.com/problemset/problem/110/A
**Limits:** 2 seconds, 256 MB

## Problem

A *lucky number* is a positive integer whose decimal digits are all `4` or `7`.
Examples: `4`, `47`, `744` are lucky. `5`, `17`, `467` are not.

A number is called *nearly lucky* if the **count of lucky digits** (4s and 7s) in it is itself a lucky number.

Given `n`, decide whether it is nearly lucky.

## Input

A single integer `n` (1 ≤ n ≤ 10^18).

## Output

Print `YES` if `n` is nearly lucky, otherwise print `NO`.

## Examples

| Input | Output | Why |
|---|---|---|
| `40047` | `NO` | 3 lucky digits, 3 is not lucky |
| `7747774` | `YES` | 7 lucky digits, 7 is lucky |
| `1000000000000000000` | `NO` | 0 lucky digits |

## Approach

1. Read `n` as a string (avoids any 64-bit integer issues).
2. Count the characters that are `4` or `7`.
3. Check that the count is positive and its digits are all `4` or `7`.

Since `n` has at most 19 digits, the count is at most 19, so only `4` and `7` qualify.

**Time complexity:** O(len(n))
**Space complexity:** O(1)

## Solution (Python)

```python
n = input().strip()
c = sum(ch in "47" for ch in n)
print("YES" if c > 0 and all(d in "47" for d in str(c)) else "NO")
```

## Solution (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    string n;
    cin >> n;
    int count = 0;
    for (char c : n)
        if (c == '4' || c == '7') count++;
    cout << (count == 4 || count == 7 ? "YES" : "NO") << endl;
    return 0;
}
```
