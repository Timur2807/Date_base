"""
В этом модуле представлены пути для авторизации пользователя приложения.
"""

from django.urls import path
from django.contrib.auth import views as standard_view

from .views import *

app_name = 'registration'

urlpatterns = [
    path('signup/', registration, name='registration'),
    path('login/', standard_view.LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('', welcome, name='welcome'),
]
