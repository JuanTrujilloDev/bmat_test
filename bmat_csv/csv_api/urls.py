from csv_api import views
from django.urls import path

urlpatterns = [
    
    path(
        "csv_tasks/", views.CSVTaskListOrCreateView.as_view(), name="csv_task_list_or_create"
    ),
    path(
        "csv_tasks/<str:task_id>/",
        views.CSVTaskDetailView.as_view(),
        name="csv_task_detail",
    ),
    path("csv_tasks/<str:task_id>/download/", views.CSVTaskDownloadView.as_view(), name="download_csv")
]
