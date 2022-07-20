import sys
sys.stdin = open("3_2070_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    print(li)

    if li[0] > li[1]:
        result = '>'
    if li[0] < li[1]:
        result = '<'
    if li[0] == li[1]:
        result = '='

    print(f'#{tc} {result}')
    