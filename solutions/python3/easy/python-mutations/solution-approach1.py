# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
# Problem     Mutations
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-18, 02:56 p.m.
# Technique   string-slicing-concatenation
# Time        O(n)
# Space       O(n)
# Insight     The function constructs a new string by concatenating the prefix before the target index, the replacement character, and the suffix starting after the target index.
# Interview   Before: "I would convert the string to a list to modify it." After: "Since strings are immutable, I use slicing to create a new string in O(n) time and space, ensuring the character at the specified position is replaced correctly."
# Pitfalls    (1) Attempting to modify the string in-place using index assignment will raise a TypeError.  (2) Incorrectly calculating the slice end index as position instead of position + 1 will result in the loss of the character at the target position.
# ──────────────────────────────────────────────────

def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1:]
    return string

