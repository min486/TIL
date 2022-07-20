import sys
sys.stdin = open("1938_input.txt", "r")

a, b = map(int, input().split())

for result in [a + b, a - b, a * b, a // b]:
    print(result)