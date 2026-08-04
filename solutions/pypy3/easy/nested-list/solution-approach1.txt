# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Problem     Nested Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    pypy3
# Status      Accepted
# Submitted   2026-08-04, 12:39 p.m.
# Technique   set-sorting-and-filtering
# Time        O(N log N)
# Space       O(N)
# Insight     The algorithm identifies the second lowest grade by extracting unique values into a sorted set and then filters the original list for students matching that specific grade.
# Interview   Before: "How would you find the second lowest value in an unsorted list?" After: "I would use a set to extract unique values, sort them, and then filter the original list, resulting in O(N log N) time complexity, which handles the requirement to sort names alphabetically for ties."
# Pitfalls    (1) Assuming the second lowest grade is always at index 1 without verifying the input contains at least two distinct grades.  (2) Failing to sort the final list of names alphabetically, which is a specific requirement for ties in the problem statement.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    grades = [student[1] for student in students]
    unique_grades=sorted(set(grades))
    second_lowest = unique_grades[1]
    names=[student[0] for student in students if student[1]==second_lowest]
    names.sort()
    for name in names:
        print(name)
