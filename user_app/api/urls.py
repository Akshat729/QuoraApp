from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import logout_view
from user_app.api.views import registration_view

# User Registration, Login and Logout URLS  #
urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout_view, name='logout'),
]


