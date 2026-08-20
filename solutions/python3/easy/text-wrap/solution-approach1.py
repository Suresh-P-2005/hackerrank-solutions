# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
# Problem     Text Wrap
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 02:46 p.m.
# Technique   string-slicing-step-iteration
# Time        O(N)
# Space       O(N)
# Insight     The implementation iterates through the string using a fixed step size equal to the maximum width, slicing segments and joining them with newline characters.
# Interview   Before: "How would you wrap a string into fixed-width lines?" After: "I would use a loop with a step size of max_width to slice the string into segments, resulting in O(N) time and space complexity, where N is the length of the input string."
# Pitfalls    (1) Failing to account for the final segment being shorter than max_width when using fixed-step slicing.  (2) Assuming the input string contains spaces, whereas this implementation treats all characters equally regardless of word boundaries.
# ──────────────────────────────────────────────────



def wrap(string, max_width):
    result = []

    for i in range(0, len(string), max_width):
        result.append(string[i:i + max_width])

    return '\n'.join(result)

