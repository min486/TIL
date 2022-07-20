import sys
sys.stdin = open("1936_input.txt", "r")

A, B = map(int, input().split())

if (A == 1 and B == 3) or (A == 2 and B == 1) or (A == 3 and B == 2):
    print('A')
else:
    print('B')