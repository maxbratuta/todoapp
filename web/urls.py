from django.urls import path
from .views import index


urlpatterns = [
    path('tasks/', index, name='tasks.index'),
]
