from django.urls import path
from .views import CreateUserView, UserDetailView, UsersDetailView, AllUsersDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/register/', CreateUserView.as_view(), name='user-create'),
    path('api/user/', UserDetailView.as_view(), name='user-detail'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/users/<int:id>', UsersDetailView.as_view(), name='users-detail'),
    path('api/users/all/', AllUsersDetailView.as_view(), name='all-users')
]


