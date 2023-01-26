from django.urls import path

from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, UserTaskCreateView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:id>/', TaskDetailView.as_view(), name='task'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:id>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:id>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:id>/select/', UserTaskCreateView.as_view(), name='task-select'),
] 