# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
# Problem     Designer Door Mat
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 03:30 p.m.
# ──────────────────────────────────────────────────

N,M = map(int,input().split())

for i in range(N//2):
    pattern = ".|."*(2*i+1)
    print(pattern.center(M,"-"))
    
print("WELCOME".center(M,"-"))

for i in range(N//2-1,-1,-1):
    pattern = ".|."*(2*i+1)
    print(pattern.center(M,"-"))
