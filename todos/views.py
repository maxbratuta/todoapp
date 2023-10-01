from django.shortcuts import render
from rest_framework import generics
from .models import Task, Project, Checklist, Notification
from .serializers import TaskSerializer, ProjectSerializer, ChecklistSerializer, NotificationSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ChecklistListCreateView(generics.ListCreateAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer


class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todos/task_list.html', {'task_list': tasks})
