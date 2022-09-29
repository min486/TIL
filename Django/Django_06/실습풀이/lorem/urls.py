from django.urls import path
from . import views

# url을 APP별로 분리하기위해
app_name = 'lorem'

urlpatterns = [
  path('', views.index),
  path('result/', views.result, name='result')
]