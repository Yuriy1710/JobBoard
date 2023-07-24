from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from home.views import *
from job.views import *
from user_profile.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', include('user_profile.urls')),
    path('jobs/', include("job.urls")),
]
