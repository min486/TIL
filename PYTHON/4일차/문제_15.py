word = input()
first = -1

for i in range(len(word)):
    if word[i] == 'a':
        first = i
        break

print(first)


# 추가 문제
word = input()

for i in range(len(word)):
    if word[i] == 'a':
        print(i, end=' ')
