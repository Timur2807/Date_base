"""
В этом модуле представлены пути для отображения API.
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'data', DataViewSet)

app_name = 'api_app'

urlpatterns = [
    path('api/v1/', include(router.urls), name='my_api'),
]
