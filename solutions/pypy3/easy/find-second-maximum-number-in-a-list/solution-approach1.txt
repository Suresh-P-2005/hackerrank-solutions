# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    pypy3
# Status      Accepted
# Submitted   2026-08-04, 11:44 a.m.
# Technique   set-max-removal
# Time        O(n)
# Space       O(n)
# Insight     The algorithm identifies the runner-up by converting the input list into a set to eliminate duplicates, removing the maximum value, and finding the new maximum.
# Interview   Before: "I could sort the list and pick the second-to-last element." After: "Using a set to filter duplicates allows finding the runner-up in O(n) time, which is more efficient than sorting, especially when handling large datasets with many duplicate scores."
# Pitfalls    (1) The code assumes the input contains at least two distinct scores, as calling remove on a set with only one element or max on an empty set will raise an error.  (2) The implementation does not handle cases where all input scores are identical, which would result in an empty set after the removal step.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores=set(arr)
    unique_scores.remove(max(unique_scores))
    runner=max(unique_scores)
    print(runner)
