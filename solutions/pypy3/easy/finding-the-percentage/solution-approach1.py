# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
# Problem     Finding the percentage
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    pypy3
# Status      Accepted
# Submitted   2026-08-04, 03:28 p.m.
# Technique   hash-map-lookup-average
# Time        O(N + M)
# Space       O(N * M)
# Insight     The implementation maps student names to lists of floating-point scores in a dictionary, allowing constant-time retrieval of the target student's marks for subsequent average calculation.
# Interview   Before: "How would you store and retrieve student records efficiently?" After: "I used a dictionary for O(1) average-case lookup time, where N is the number of students and M is the number of scores per student, resulting in O(N*M) space complexity to store all records."
# Pitfalls    (1) Failing to convert input strings to floats, which causes a TypeError during the sum operation.  (2) Assuming the query_name always exists in the dictionary, which would raise a KeyError if the input name is missing.  (3) Incorrectly formatting the output string, as the problem requires exactly two decimal places.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    
    print(f"{average:.2f}")
