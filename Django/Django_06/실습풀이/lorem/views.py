from django.shortcuts import render
import random

def index(request):
  return render(request,'lorem/index.html')

def result(request):
  word_list = ['돼지', '말', '소', '오리', '닭']
  paragraph = int(request.GET.get('paragraph'))
  word = int(request.GET.get('word'))

  lorem_para = []
  
  # 입력한 문단의 수 만큼 랜덤으로 단어를 추출하는 반복문을 반복
  for _ in range(paragraph):
    # 입력한 단어의 수 만큼 랜덤으로 단어를 추출하는 반복
    string = ""
    for _ in range(word):
      string += random.choice(word_list) + " "

    lorem_para.append(string)
  
  context = {
    "lorem_para" : lorem_para,
  }

  return render(request, 'lorem/result.html',context)