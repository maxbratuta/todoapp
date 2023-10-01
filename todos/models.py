from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()


class Checklist(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)


class Notification(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
