# 281A - Word Capitalization

**Platform:** Codeforces
**Problem:** [281A](https://codeforces.com/problemset/problem/281/A)
**Difficulty:** 800
**Tags:** implementation, strings
**Time limit:** 2 seconds
**Memory limit:** 256 megabytes

---

## Problem Statement

Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note that during capitalization all the letters except the first one remain unchanged.

### Input

A single line contains a non-empty word. The word consists of lowercase and uppercase English letters. The length of the word will not exceed 10^3.

### Output

Output the given word after capitalization.

### Examples

| Input    | Output   |
|----------|----------|
| `ApPLe`  | `ApPLe`  |
| `konjac` | `Konjac` |

---

## Approach

1. Read the word.
2. Convert only the first character to uppercase.
3. Keep the rest of the string exactly as it is.
4. Print the result.

### Common Trap

Python's `str.capitalize()` uppercases the first letter but **lowercases the rest**.

```python
"ApPLe".capitalize()      # "Apple"  -> wrong
"ApPLe"[0].upper() + "ApPLe"[1:]   # "ApPLe" -> correct
```

The problem says all other letters must remain unchanged, so slicing is the right tool.

---

## Solutions

### Python

```python
s = input()
print(s[0].upper() + s[1:])
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    s[0] = toupper(s[0]);
    cout << s << "\n";
    return 0;
}
```

---

## Complexity

- **Time:** O(n), where n is the length of the word
- **Space:** O(n)

---

## Key Takeaways

- Read the statement carefully: "all other letters remain unchanged" rules out `capitalize()` in Python.
- `s[0].upper() + s[1:]` is the standard pattern for changing only the first character.
- In C++, strings are mutable, so `s[0] = toupper(s[0])` edits in place.
