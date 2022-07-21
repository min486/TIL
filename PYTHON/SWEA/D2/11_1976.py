import sys
sys.stdin = open("11_1976_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())

    sum_h = h1 + h2
    sum_m = m1 + m2

    if sum_m >= 60:
        sum_m -= 60
        sum_h += 1
    if sum_h > 12:
        sum_h -= 12

    print(f'#{tc} {sum_h} {sum_m}')

        


