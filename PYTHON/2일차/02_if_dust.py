# dust = int(input())

# if dust > 0 and dust <= 30:
#     print('좋음')
# elif dust > 30 and dust <= 80:
#     print('보통')
# elif dust > 80 and dust <= 150:
#     print('나쁨')
# else:
#     print('매우나쁨')

dust = 100

# dust가 150보다 크면, 매우 나쁨
if dust > 150:
    print('매우 나쁨')
# 80보다 크면, 나쁨
elif dust > 80:
    print('나쁨')
# 30보다 크면, 보통
elif dust > 30:
    print('보통')
# 좋은
# else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능
else:
    print('좋음')

    
# 150 >= dust > 80
# 80 >= dust > 30으로 작성할 필요가 있을까?
# -> 가능하지만 굳이 필요가 없다. 왜냐하면 위에서부터 아래로 순차적으로 실행되기 때문
