from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Login logic
    path('administrator/', views.logon_admin, name='admin_panel'),
]