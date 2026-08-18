# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
# Problem     Mutations
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-18, 02:56 p.m.
# ──────────────────────────────────────────────────

def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1:]
    return string

