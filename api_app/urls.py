from django.urls import path
from .views import *

app_name = 'api_app'

urlpatterns = [
    path('api/', DataAPIView.as_view(), name='my_api'),
]
