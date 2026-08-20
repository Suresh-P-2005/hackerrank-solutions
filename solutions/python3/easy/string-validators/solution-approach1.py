# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
# Problem     String Validators
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 12:21 p.m.
# Technique   generator-expression-any-check
# Time        O(N)
# Space       O(1)
# Insight     The solution uses generator expressions with the any function to perform a short-circuiting linear scan for each character property across the input string.
# Interview   Before: "I would iterate through the string and maintain five boolean flags." After: "Using any with generator expressions is more idiomatic and efficient, achieving O(N) time complexity by stopping as soon as a match is found for each condition."
# Pitfalls    (1) Confusing the any function with all, which would incorrectly require every character in the string to satisfy the condition.  (2) Assuming the built-in methods check the entire string rather than individual characters when used inside a generator expression.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    s = input()
    
    print(any(ch.isalnum() for ch in s))
    print(any(ch.isalpha() for ch in s))
    print(any(ch.isdigit() for ch in s))
    print(any(ch.islower() for ch in s))
    print(any(ch.isupper() for ch in s))
