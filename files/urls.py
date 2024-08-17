from django.urls import path
from .views import *

app_name = 'files'

urlpatterns = [
    path('upload/', my_files, name='file_upload'),
    path('files/', my_file_list, name='file_list'),
    path('file/<int:pk>/', file_view, name='file_details'),

]
