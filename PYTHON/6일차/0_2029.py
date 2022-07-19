import sys
sys.stdin = open("0_2029_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    mok = a // b
    re = a % b
    print(f'#{tc} {mok} {re}')

