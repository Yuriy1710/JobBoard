from django.urls import path
from . import views

urlpatterns = [
    path('<int:job_id>/', views.job_detail, name="job_detail"),
    path('<int:job_id>/apply_for_job/', views.apply_for_job, name="apply_for_job"),
    path('add/', views.add_job, name='add_job'),
]
