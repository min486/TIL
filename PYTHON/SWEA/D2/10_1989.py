import sys
sys.stdin = open("10_1989_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    word = input()

    if word[::] == word[::-1]:
        result = 1
    else:
        result = 0
    
    print(f'#{tc} {result}')

