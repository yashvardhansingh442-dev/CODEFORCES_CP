# 266A - Stones on the Table

**Platform:** Codeforces
**Difficulty:** 800
**Tags:** implementation
**Time Limit:** 2 seconds
**Memory Limit:** 256 MB

---

## Problem Statement

There are `n` stones on the table in a row, each of them can be red, green or blue. Count the minimum number of stones to take from the table so that any two neighboring stones had different colors. Stones in a row are considered neighboring if there are no other stones between them.

## Input

- The first line contains an integer `n` (1 ≤ n ≤ 50), the number of stones on the table.
- The next line contains a string `s`, which represents the colors of the stones. Each character is `R`, `G`, or `B` (red, green, blue). The `i`-th character of the string is the color of the `i`-th stone from left to right.

## Output

Print a single integer: the answer to the problem.

## Examples

### Example 1

**Input**
```
3
RRG
```

**Output**
```
1
```

### Example 2

**Input**
```
5
RRRRR
```

**Output**
```
4
```

### Example 3

**Input**
```
4
BRBG
```

**Output**
```
0
```

---

## Approach

Whenever `s[i] == s[i-1]`, one of the two stones must be removed. Count all such positions. Removing a stone from a run of equal colors never creates a new conflict, so the count is the minimum.

## Solution (Python)

```python
n = int(input())
s = input().strip()

count = 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        count += 1

print(count)
```

## Solution (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    string s;
    cin >> n >> s;

    int count = 0;
    for (int i = 1; i < n; i++) {
        if (s[i] == s[i - 1]) count++;
    }

    cout << count << endl;
    return 0;
}
```

## Complexity

- **Time:** O(n)
- **Space:** O(1) (besides the input string)
