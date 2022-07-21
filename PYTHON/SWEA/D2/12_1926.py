import sys
sys.stdin = open("12_1926_input.txt", "r")

N = int(input())
clap = ['3', '6', '9']

for i in range(1, N + 1):
    cnt = 0
    for j in str(i):
        if j in clap:
            cnt += 1

    if cnt > 0:
        i = '-' * cnt

    print(i, end = ' ')