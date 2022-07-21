import sys
sys.stdin = open("2043_input.txt", "r")

p, k = map(int, input().split())
cnt = 0
for i in range(k, p + 1):
    cnt += 1

print(cnt)
