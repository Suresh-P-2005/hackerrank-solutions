# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
# Problem     Find a string
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-18, 03:44 p.m.
# Technique   sliding-window-substring-count
# Time        O(N*M)
# Space       O(M)
# Insight     The algorithm iterates through all possible starting positions where the substring could fit, checking for a match at each window of length equal to the substring.
# Interview   Before: "I would use the built-in count method." After: "I implemented a sliding window to manually count overlapping occurrences, which runs in O(N*M) time where N is the string length and M is the substring length, correctly handling the case-sensitive requirement."
# Pitfalls    (1) The loop range must be len(string) - len(sub_string) + 1 to ensure the final possible window is checked.  (2) Failing to account for overlapping occurrences by using string.count() instead of a manual sliding window.
# ──────────────────────────────────────────────────

def count_substring(string, sub_string):
    count = 0
    for i in range (len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]==sub_string:
            count+=1
    return count

