from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm
from .models import TodoItem


def register(request):
    """
    User Registration form
    Args:
        request (POST): New user registered
    """
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "todo/register.html", context)


@login_required
def home(request):
    """
    Create todo item and view other todo items as well.
    """
    if request.method == 'POST':
        todo_name = request.POST.get("new-todo")
        todo = TodoItem.objects.create(name=todo_name, user=request.user)
        return redirect("home")

    # retrieving todo items which are incomplete
    # todos = TodoItem.objects.filter(user=request.user, is_completed=False).order_by("-id")
    todos = TodoItem.objects.filter(user=request.user).order_by("-id")

    return render(request, "todo/crud.html", context={
        "todos": todos,
        "page_obj": Paginator(todos, 4).get_page(number=request.GET.get("page"))
    })


def update_todo(request, pk):
    """
    Update todo item
    Args:
        pk (Integer): Todo ID - primary key
    """
    # NOTE: below get_object_or_404() returns a data if exists else status 404 not found
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)

    # NOTE: request.POST.get("todo_{pk}") is the input name of the todo modal
    todo.name = request.POST.get(f"todo_{pk}")
    todo.save()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_todo(request, pk):
    """
    Delete todo item
    Args:
        pk (Integer): Todo ID - Primary key
    """
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def complete_todo(request, pk):
    """
    Updating todo as completed item
    Args:
        pk (Integer): Todo ID - primary key
    """
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))