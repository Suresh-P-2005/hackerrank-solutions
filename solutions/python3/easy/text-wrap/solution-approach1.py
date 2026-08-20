# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
# Problem     Text Wrap
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 02:46 p.m.
# ──────────────────────────────────────────────────



def wrap(string, max_width):
    result = []

    for i in range(0, len(string), max_width):
        result.append(string[i:i + max_width])

    return '\n'.join(result)

