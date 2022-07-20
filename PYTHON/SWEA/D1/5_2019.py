import sys
sys.stdin = open("5_2019_input.txt", "r")

n = int(input())

for i in range(n + 1):
    result = 2 ** i
    print(result, end = ' ')
