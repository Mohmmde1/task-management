from django.urls import path
from .views import TaskCreateView, TaskListView, TaskRetrieveView, TaskDeleteView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveView.as_view(), name='task-retrieve'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
