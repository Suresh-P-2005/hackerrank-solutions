# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
# Problem     String Split and Join
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-18, 02:28 p.m.
# Technique   split-and-join-string-methods
# Time        O(N)
# Space       O(N)
# Insight     The implementation utilizes built-in string methods to tokenize the input by space characters and reconstruct the sequence using a hyphen delimiter.
# Interview   Before: "How would you transform a space-separated string into a hyphenated one?" After: "I used split and join methods, which operate in O(N) time and space, where N is the length of the string, to efficiently handle the delimiter replacement."
# Pitfalls    (1) Using split() without the explicit " " argument would cause the method to split on any whitespace, potentially altering the expected output for multiple spaces.  (2) Assuming the input string contains no spaces will result in a single-element list, which join() will return unchanged.
# ──────────────────────────────────────────────────

def split_and_join(line):
    # write your code here
    words = line.split(" ")
    result = "-".join(words)
    return result

