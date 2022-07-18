# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# 오류
## or 연산자는 비교 연산자가 아니라 bool 타입 연산자이므로 char의 타입을 따지는 조건문 말고 값을 따지는 조건문을 적어준다

# 수정
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)