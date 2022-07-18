N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

# 원인
## append()는 튜플(())이 아닌 리스트([])에서 사용 가능하다

# 수정
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)