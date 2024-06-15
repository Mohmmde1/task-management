from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDeleteView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
