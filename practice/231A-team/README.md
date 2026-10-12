# 231A. Team

**Platform:** Codeforces | **Difficulty:** ~800 | **Tags:** greedy, brute force

## Problem

Three friends (Petya, Vasya and Tonya) are taking part in a contest with `n`
problems. They only attempt a problem if **at least two of them** are sure
about the solution.

Given each friend's confidence for every problem, count how many problems
they will attempt.

## Input

- The first line contains an integer `n` (1 ≤ n ≤ 1000), the number of problems.
- Each of the next `n` lines contains three integers (each `0` or `1`).
  A `1` means that friend is sure about the solution, and `0` means they are not.
  The three numbers are for Petya, Vasya and Tonya, in that order.

## Output

Print a single integer: the number of problems the friends will attempt.

## Example

Input:
3
1 1 0
1 1 1
1 0 0

Output:
2

(Problems 1 and 2 have at least two `1`s; problem 3 has only one.)

## Link

https://codeforces.com/problemset/problem/231/A
