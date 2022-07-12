numbers = [0, 100, -10, 20, 5]
numbers.sort()
max = numbers[0]
list = []

for i in numbers:
    if max <= i:
        max = i
        list.append(max)

print(list[-2])