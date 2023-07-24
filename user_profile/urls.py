from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('application/<int:application_id>/', views.view_application, name='view_application'),
    path('job/<int:job_id>/', views.view_dashboard_job, name="view_dashboard_job")
]
