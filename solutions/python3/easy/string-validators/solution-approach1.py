# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
# Problem     String Validators
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 12:21 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    s = input()
    
    print(any(ch.isalnum() for ch in s))
    print(any(ch.isalpha() for ch in s))
    print(any(ch.isdigit() for ch in s))
    print(any(ch.islower() for ch in s))
    print(any(ch.isupper() for ch in s))
