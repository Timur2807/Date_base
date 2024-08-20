"""
В этом модуле представлены пути для авторизации пользователя приложения.
"""

from django.urls import path
from django.contrib.auth.views import LoginView

from .views import *

app_name = 'registration'

urlpatterns = [
    path('signup/', registration, name='registration'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', logout_user, name='logout'),
    path('', welcome, name='welcome'),
]
