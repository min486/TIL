import sys
sys.stdin = open("2025_input.txt", "r")

n = int(input())
total = 0

for i in range(1, n + 1):
    total += i

print(total)
