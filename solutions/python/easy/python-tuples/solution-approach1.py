# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Problem     Tuples 
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python
# Status      Accepted
# Submitted   2026-08-04, 04:02 p.m.
# Technique   tuple-hashing-from-input
# Time        O(n)
# Space       O(n)
# Insight     The implementation converts a space-separated string of integers into a tuple and computes its hash value using the built-in hash function.
# Interview   Before: "How would you compute the hash of a sequence of integers?" After: "I would map the input string to integers, cast them to a tuple, and call hash(). This runs in O(n) time and space, where n is the number of elements provided in the input."
# Pitfalls    (1) Using input() instead of raw_input() in Python 2 environments can cause syntax errors.  (2) Failing to map the split string elements to integers before creating the tuple results in a tuple of strings, which produces a different hash value.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))
