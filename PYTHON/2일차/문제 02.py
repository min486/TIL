word = 'happy!'
sum = 0

# 1) while문
while sum < 6:
    sum += 1
print(sum)

# 2) for문(문자열 그대로)
for i in word:
    sum += 1
print(sum)

# 3) for문(index)
for i in range(6):
    sum += 1
print(sum)