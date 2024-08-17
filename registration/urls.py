from django.urls import path

from .views import *

app_name = 'registration'

urlpatterns = [
    path('signup/', registration, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('welcome/', welcome, name='welcome'),
]
