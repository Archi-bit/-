from django.urls import URLPattern, path
from .views import TaskListView, TaskDetailView, TaskCreateView
from . import views

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("complete/<int:pk>/", views.task_complete, name="task_complete"),
    path("delete/<int:pk>/", views.task_delete, name="task_delete"),
]