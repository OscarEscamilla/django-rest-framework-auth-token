from django.urls import path

from server.auth import api

urlpatterns = [
    path('api/v1/login', api.login, name = 'login'),
    path('api/v1/signup', api.register, name = 'signup'),
    path('api/v1/profile', api.profile, name = 'profile'),
]