from django.db import models
from django.conf import settings


class TodoItem(models.Model):
    """
    Todo Item Model
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="todo_item"
    )

    name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta Information
        """
        app_label = "todo"
        db_table = "todo_item"
        verbose_name = "todo_item"
        verbose_name_plural = "todo_items"

    def __str__(self):
        return self.name