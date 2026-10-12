# 71A. Way Too Long Words

**Platform:** Codeforces | **Difficulty:** ~800 | **Tags:** strings

## Problem

A word is "too long" if it has **more than 10 characters**. Every too-long
word must be replaced by an abbreviation: the first letter, then the number
of letters between the first and last letters, then the last letter.

Words that are not too long stay unchanged.

For example, `localization` becomes `l10n` and `internationalization`
becomes `i18n`.

## Input

- The first line contains an integer `n` (1 ≤ n ≤ 100), the number of words.
- Each of the next `n` lines contains one word of lowercase Latin letters,
  with length from 1 to 100.

## Output

Print `n` lines, where the i-th line is the result of processing the i-th word.

## Example

Input:
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis

Output:
word
l10n
i18n
p43s

## Link

https://codeforces.com/problemset/problem/71/A
