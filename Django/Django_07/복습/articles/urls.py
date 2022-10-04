from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # http://127.0.0.1:8000/articles/1/ : 1번글
    # http://127.0.0.1:8000/articles/3/ : 3번글
    path('<int:pk>/', views.detail, name='detail'),
]