n = 10
result = 0

# 1) while문
i = 0
while i <= n:
    result += i
    i += 1
print(result)

# 2) for문
for i in range(n+1):
    result += i
print(result)