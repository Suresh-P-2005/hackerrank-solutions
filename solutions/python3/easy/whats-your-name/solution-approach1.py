# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
# Problem     What's Your Name?
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-18, 02:44 p.m.
# Technique   f-string-interpolation
# Time        O(N+M)
# Space       O(N+M)
# Insight     The function utilizes Python f-string formatting to concatenate the provided first and last name strings into the required output template.
# Interview   Before: 'How do I combine strings with variables?' After: 'Use f-strings for O(N+M) time complexity, where N and M are the lengths of the input strings, ensuring the exact punctuation required by the problem statement is preserved.'
# Pitfalls    (1) Using incorrect variable names first_name and last_name instead of the function parameters first and last.  (2) Failing to include the required exclamation mark before the phrase You just delved into python.  (3) Omitting the period at the end of the required output string.
# ──────────────────────────────────────────────────

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first_name} {last_name}! You just delved into python.")

