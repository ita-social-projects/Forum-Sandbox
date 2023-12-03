from django.urls import path
from .views import CreateUserView, UserDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/register/', CreateUserView.as_view(), name='user-create'),
    path('api/user/', UserDetailView.as_view(), name='user-detail'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]


