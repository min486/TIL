import sys
sys.stdin = open("1_1545_input.txt", "r")

num = int(input())

for i in range(num, -1, -1):
    print(i, end = " ")
