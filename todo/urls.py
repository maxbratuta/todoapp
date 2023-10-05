from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (register, home, update_todo, delete_todo, toggle_todo_status)

urlpatterns = [
    path("login/", LoginView.as_view(template_name="todo/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="todo/logout.html"), name="logout"),
    path("register/", register, name="register"),

    path("", home, name="home"),

    path("update/todo/<int:pk>/", update_todo, name="update_todo"),
    path("complete/todo/<int:pk>/", toggle_todo_status, name="toggle_todo_status"),
    path("delete/todo/<int:pk>/", delete_todo, name="delete_todo"),
]