from django.contrib import admin
from django.urls import path, include 
from .views import CreateTaskView, TaskListView, EditTaskView, complete_task, DeleteTaskView, CompletedTaskListView

urlpatterns = [
    path('', CreateTaskView.as_view(), name='home'),
    path('task-list/', TaskListView.as_view(), name='task_list'),
    path('completed-task-list/', CompletedTaskListView.as_view(), name='completed_task_list'),
    path('edit-task/<int:pk>/', EditTaskView.as_view(), name='edit_task'),
    path('complete-task/<int:pk>/', complete_task, name='complete_task'),
    path('delete-task/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
]