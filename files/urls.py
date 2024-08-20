"""
В этом модуле представлены пути для приложения files.
"""

from django.urls import path
from .views import *

app_name = 'files'

urlpatterns = [
    path('upload/', about, name='file_upload'),
    path('files/', file_list, name='file_list'),
    path('file/<int:pk>/', file_view, name='file_details'),

]
