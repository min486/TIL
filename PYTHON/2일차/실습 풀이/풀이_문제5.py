# 평균 구하기
# result, count 둘다 해나가는것이 핵심

# 1. 문제 제공
numbers = [3, 10, 20]
result = 0
count = 0

# 2. 값 초기화
result = 0
count = 0

# 3. 반복
for number in numbers:
    result =  result + number
    # result += number
    count = count + 1
    # count += 1

print(result/count)
# print(sum(numbers)/len(numbers))
# >> 한줄 정답