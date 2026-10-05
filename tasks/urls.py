from django.urls import path
from .views import task_list, update_task, delete_task

urlpatterns = [
    path("", task_list, name="task_list"),
    path("update/<int:task_id>/", update_task, name="update_task"),
    path("delete/<int:task_id>/", delete_task, name="delete_task"),
]