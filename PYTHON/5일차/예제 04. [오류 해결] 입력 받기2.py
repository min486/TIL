# words = list(map(int, input().split()))
# print(words)

# 원인
## 값 에러, int로 바꿀 수 없는 값(문자)이 들어가있다

# 수정
words = int, input().split()
print(words)
