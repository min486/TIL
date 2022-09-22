from django.shortcuts import render
import random

# Create your views here.

def lotto(request):
    # 당첨 번호
    win_num = [11, 22, 33, 39, 41, 44]
    row_li = []

    for i in range(5):
        lotto = random.sample(range(1, 46), 5)
        cnt = 0
        
        for lo in lotto:
            if lo in win_num:
                cnt += 1

        if cnt == 6:
            result = 1
        elif cnt == 5:
            result = 2
        elif 2 <= cnt <= 4:
            result = 3
        elif cnt == 1:
            result = 4
        else:
            result = 5
            
        # [[[11, 22, 33], 4], [[11, 22, 33], 5]]
        row_li.append([sorted(lotto), result])  

    context = {
        # 변수명: 값
        'num_rank': row_li, 
    }

    return render(request, 'lotto.html', context)