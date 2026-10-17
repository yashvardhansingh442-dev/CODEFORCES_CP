# Codeforces 112A: Petya and Strings

- **Rating:** 800
- **Tags:** implementation, strings
- **Link:** https://codeforces.com/problemset/problem/112/A

## Problem (short)

Given two strings of equal length made of Latin letters, compare them
lexicographically **ignoring case**.

- Print `-1` if the first string is smaller
- Print `1` if the first string is larger
- Print `0` if they are equal

## Example

| Input | Output |
|-------|--------|
| `aaaa` / `aaaA` | `0` |
| `abs` / `Abz` | `-1` |
| `abcdefg` / `AbCdEfF` | `1` |

## Approach

1. Convert both strings to lowercase.
2. Compare them directly with `<` and `>`.

Lexicographic comparison is built into both Python and C++ strings, so no manual loop is needed.

**Time:** O(n) **Space:** O(n)

## Python

```python
a = input().lower()
b = input().lower()

if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)
```

## C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    transform(a.begin(), a.end(), a.begin(), ::tolower);
    transform(b.begin(), b.end(), b.begin(), ::tolower);

    if (a < b) cout << -1;
    else if (a > b) cout << 1;
    else cout << 0;

    return 0;
}
```

## Key Learnings

- Normalize case before comparing (`lower()` / `tolower`).
- Strings compare lexicographically with `<`, `>`, `==`.
- Uppercase letters have smaller ASCII values than lowercase, so comparing without normalizing gives wrong answers.

## Self-Check Questions

1. Why does comparing `"Z"` and `"a"` without lowercasing give the wrong answer?
2. What would change if the strings had different lengths?
3. Can you solve it without `lower()`, using a character-by-character loop?
4. What is the time complexity, and why?


## My Notes

- [ ] Solved in Python
- [ ] Solved in C++
- [ ] Revisited after 1 week
