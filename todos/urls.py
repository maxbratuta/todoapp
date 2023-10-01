from django.urls import path
from .views import TaskListCreateView, ProjectListCreateView, ChecklistListCreateView, NotificationListCreateView

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("projects/", ProjectListCreateView.as_view(), name="project-list-create"),
    path("checklists/", ChecklistListCreateView.as_view(), name="checklist-list-create"),
    path("notifications/", NotificationListCreateView.as_view(), name="notification-list-create"),
]
