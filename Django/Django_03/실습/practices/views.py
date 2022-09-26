from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.

def odd_even(request, num):
    if num % 2 == 1:
        result = f'{num}은(는) 홀수 입니다'
    elif num == 0:
        result = f'{num}은(는) 0 입니다'
    else:
        result = f'{num}은(는) 짝수 입니다'

    context = {
        'confirm': result
    }

    return render(request, 'odd_even.html', context)

def four_count(request, num1, num2):
    li = []
    li.append(f'{num1} + {num2} = {num1 + num2}')
    li.append(f'{num1} - {num2} = {num1 - num2}')
    li.append(f'{num1} * {num2} = {num1 * num2}')
    li.append(f'{num1} // {num2} = {num1 // num2}')

    context = {
        'result': li
    }

    return render(request, 'four.html', context)

def maplestory(request):

    context = {
        'img': 'https://ssl.nexon.com/s2/game/maplestory/renewal/common/media/artwork/artwork_87.jpg',
    }
    
    return render(request, 'maple.html', context)

def maple_image(request):

    _name = request.GET.get('input_name')

    imgs = [
        'https://ssl.nexon.com/s2/game/maplestory/renewal/common/media/artwork/artwork_75.jpg',
        'https://ssl.nexon.com/s2/game/maplestory/renewal/common/media/artwork/artwork_78.jpg',
        'https://ssl.nexon.com/s2/game/maplestory/renewal/common/media/artwork/artwork_35.jpg',
        'https://ssl.nexon.com/s2/game/maplestory/renewal/common/media/artwork/artwork_13.jpg',
        'https://lwi.nexon.com/maplestory/common/media/artwork/artwork_107.jpg',
    ]

    _img = random.choice(imgs)

    context = {
        'name': _name,
        'img' : _img,
    }

    return render(request, 'maple2.html', context)