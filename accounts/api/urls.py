from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from accounts.api.views import (
    UserAPIView,
    UserDetailsAPIView,
    UserLoginAPIView,
    ProfileAPIView,
    ProfileDetailsAPIView,
)

app_name = 'accounts-api'

urlpatterns = [
    # token maker
    path('get-token/', obtain_auth_token),

    # basic user login, info urls
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('user/', UserAPIView.as_view(), name="user"),
    path('user/<username>/', UserDetailsAPIView.as_view(), name="user-details"),

    # user profile related urls
    path('profile/', ProfileAPIView.as_view(), name="profile"),
    path('profile/<int:pk>/', ProfileDetailsAPIView.as_view(), name="profile-details"),
]
