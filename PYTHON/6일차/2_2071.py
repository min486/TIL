import sys
sys.stdin = open("2_2071_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    ten = map(int, input().split())
    total = 0

    for i in ten:
        total += i

    result = total / 10
    print(f'#{tc} {result:.0f}')
    