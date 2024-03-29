from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:todo_pk>', views.delete, name='delete'),
    path('change/<int:change_pk>', views.change, name='change'),
]