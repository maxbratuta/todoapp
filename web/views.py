from django.shortcuts import render
from todos.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {'task_list': tasks})
