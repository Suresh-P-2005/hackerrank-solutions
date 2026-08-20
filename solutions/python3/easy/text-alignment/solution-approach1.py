# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true
# Problem     Text Alignment
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 02:07 p.m.
# Technique   string-alignment-formatting
# Time        O(thickness^2)
# Space       O(thickness)
# Insight     The implementation constructs the logo by iteratively applying string alignment methods to segments of the character 'H' based on the provided thickness parameter.
# Interview   Before: "How do I handle variable-width ASCII art?" After: "I use Python's string alignment methods like rjust, ljust, and center to maintain symmetry. This approach runs in O(thickness^2) time, as each row's length is proportional to the thickness input."
# Pitfalls    (1) Incorrectly calculating the padding width for the center method, which must account for the total width of the logo segment.  (2) Failing to ensure the thickness input is an odd number, which disrupts the symmetry of the cone and middle belt sections.  (3) Miscalculating the range bounds for the pillars and middle belt, leading to an incorrect number of rows in the final output.
# ──────────────────────────────────────────────────

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
