from django.contrib import admin

from todos.models import Task, Project


admin.site.register(Project)
admin.site.register(Task)
