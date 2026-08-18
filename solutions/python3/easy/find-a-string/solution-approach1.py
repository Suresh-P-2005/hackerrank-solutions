# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
# Problem     Find a string
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-18, 03:44 p.m.
# ──────────────────────────────────────────────────

def count_substring(string, sub_string):
    count = 0
    for i in range (len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]==sub_string:
            count+=1
    return count

