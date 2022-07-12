n = 5
i = 1
result = 1

# 1) while문
while i <= n:
    result *= i
    i += 1
print(result)

# 2) for문
for i in range(1, n+1):
    result *= i
print(result)
