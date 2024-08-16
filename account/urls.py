from django.urls import path

from .views import *


app_name = 'account'

urlpatterns = [
    path('account/', index, name='index'),
    path('my_files/', my_files, name='my_files'),
]

