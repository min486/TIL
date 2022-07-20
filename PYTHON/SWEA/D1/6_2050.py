# 아스키 코드 변환
## ord(문자) -> 정수 반환
## chr(숫자) -> 문자 반환
### A 65 / B 66 ~ / a 97 / b 98 ~

import sys
sys.stdin = open("6_2050_input.txt", "r")

al = list(input())

for i in al:
    print(ord(i)-64, end = ' ')


