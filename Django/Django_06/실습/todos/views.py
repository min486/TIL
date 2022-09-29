from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    all = Todo.objects.order_by("id")

    context = {
        "todos": all,
    }

    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get("input_todo")
    content2 = request.GET.get("input_rank")
    content3 = request.GET.get("input_deadline")

    Todo.objects.create(
        todo = content, 
        rank = content2, 
        deadline = content3
    )

    return redirect('todos:index')

def change(request, change_pk):
    pk = Todo.objects.get(pk = change_pk)
    # if pk.status:
    #     pk.status = False
    # else:
    #     pk.status = True

    # True -> False
    # False -> True
    pk.status = not pk.status
    pk.save()

    return redirect('todos:index')


def delete(request, todo_pk):
    pk = Todo.objects.get(pk = todo_pk)
    pk.delete()

    return redirect('todos:index')