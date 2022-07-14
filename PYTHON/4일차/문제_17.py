# 문자 - 유니코드 숫자 (변환)
# ord(''), chr() 

word = input()

for i in range(len(word)):
    result = chr(ord(word[i]) - 32)
    print(result, end = '')