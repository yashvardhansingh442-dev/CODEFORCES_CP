# Codeforces 236A: Boy or Girl

**Problem:** [236A on Codeforces](https://codeforces.com/problemset/problem/236/A)
**Difficulty:** 800
**Tags:** brute force, implementation, strings
**Language:** Python 3

## Problem Statement

A boy on a social network decides the gender of a user from their username:

- If the number of **distinct characters** in the username is **odd**, the user is male.
- If the number of distinct characters is **even**, the user is female.

Given a username, print `CHAT WITH HER!` if the user is female, otherwise print `IGNORE HIM!`.

## Input

A single non-empty string of lowercase English letters (at most 100 characters).

## Output

- `CHAT WITH HER!` if the user is female
- `IGNORE HIM!` if the user is male

## Examples

| Input        | Distinct letters | Output           |
|--------------|------------------|------------------|
| `wjmzbmr`    | 6                | `CHAT WITH HER!` |
| `xiaodao`    | 5                | `IGNORE HIM!`    |
| `sevenkplus` | 8                | `CHAT WITH HER!` |

## Approach

1. Read the username.
2. Convert it to a `set` to remove duplicate characters.
3. Check whether the size of the set is even or odd.
4. Print the matching message.

## Solution

```python
s = input().strip()
print("CHAT WITH HER!" if len(set(s)) % 2 == 0 else "IGNORE HIM!")
```

## Complexity

- **Time:** O(n), where n is the length of the string
- **Space:** O(1), since the set holds at most 26 characters


```

Then type a username and press Enter.
