# 266B - Queue at the School

**Platform:** Codeforces
**Difficulty:** 800
**Tags:** constructive algorithms, implementation, graph matchings

## Problem Statement

During the break the schoolchildren, boys and girls, formed a queue of `n` people in the canteen. Initially the children stood in the order they entered the canteen. After a while the boys started feeling awkward for standing in front of the girls in the queue, and they started letting the girls move forward each second.

Positions in the queue are numbered from `1` to `n`, and the person in position `1` is served first. If at time `x` a boy stands on the `i`-th position and a girl stands on the `(i + 1)`-th position, then at time `x + 1` the `i`-th position will have a girl and the `(i + 1)`-th position will have a boy.

Given the initial arrangement, determine how the queue looks after `t` seconds.

## Input

- First line: two integers `n` and `t` (1 ≤ n, t ≤ 50).
- Second line: string `s`. If the `i`-th character is `B`, that position holds a boy, otherwise (`G`) a girl.

## Output

Print string `a` describing the arrangement after `t` seconds, using `B` for a boy and `G` for a girl.

## Examples

| Input | Output |
|-------|--------|
| `5 1`<br>`BGGBG` | `GBGGB` |
| `5 2`<br>`BGGBG` | `GGBGB` |
| `4 1`<br>`GGGB` | `GGGB` |

## Approach

Simulate the process for `t` seconds. In each second, scan left to right. When `BG` is found at positions `i` and `i + 1`, swap them and skip ahead by one extra index.

The skip is needed because all swaps in one second happen **simultaneously**. Without it, a boy could keep moving forward within the same second (`BGG` would become `GGB` after one second instead of the correct `GBG`).

## Complexity

- **Time:** O(n · t)
- **Space:** O(n)

## Solution (Python)

```python
n, t = map(int, input().split())
s = list(input())

for _ in range(t):
    i = 0
    while i < n - 1:
        if s[i] == 'B' and s[i + 1] == 'G':
            s[i], s[i + 1] = s[i + 1], s[i]
            i += 2  # skip so the boy isn't moved again this second
        else:
            i += 1

print("".join(s))
```

## Solution (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, t;
    string s;
    cin >> n >> t >> s;

    while (t--) {
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == 'B' && s[i + 1] == 'G') {
                swap(s[i], s[i + 1]);
                i++;  // skip the swapped pair
            }
        }
    }

    cout << s << endl;
    return 0;
}
```

## Walkthrough (Sample 2)

`n = 5, t = 2, s = BGGBG`

- Second 1: swap positions 1-2 and 4-5 → `GBGGB`
- Second 2: swap positions 2-3 → `GGBGB`

Result: `GGBGB` ✔

## Notes

- Never let a boy move more than one position per second.
- Strings with no `BG` pair (e.g. `GGGB`) stay unchanged.
