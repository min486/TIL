# numbers = input().split()
# print(sum(numbers))


# 원인
## 타입에러, sum()은 int에서 쓸수있는 함수인데 입력 받은 것은 문자

# 수정
numbers = map(int,input().split())
print(sum(numbers))
