from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    _todos = Todo.objects.all()
    context = {
        "todos": _todos,
    }

    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get("input_content")
    Todo.objects.create(content=content)

    return redirect('todos:index')

def delete(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    todo.delete()

    return redirect('todos:index')
