a, b = map(int, input().split())

width = a * b
ver = (a + b) * 2

def rectangle(a, b):
    return width, ver

result = rectangle(a, b)
print()
