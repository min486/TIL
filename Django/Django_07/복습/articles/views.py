from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    # DB에서 가져와서
    articles = Article.objects.order_by('-pk')
    # Template에 전달한다
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form': article_form
#     }
#     return render(request, 'articles/new.html', context=context)

# new와 create 함수 합치기
def create(request):
    # form에서 글쓰기를 누르면 실행
    if request.method == 'POST': 
        # 입력받은 데이터들 DB에 저장
        article_form = ArticleForm(request.POST)
        # 유효할 경우 실행 (valid)
        if article_form.is_valid():
            article_form.save()
            # index 페이지로 redirect
            return redirect('articles:index')
    # 'GET' method 일때
    # http://127.0.0.1:8000/articles/create 일때 실행
    else:
        article_form = ArticleForm()
    # 유효하지 않을 경우 아래로 이동 (invalid)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)

def detail(request, pk):
    # 특정 글을 가져온다
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

