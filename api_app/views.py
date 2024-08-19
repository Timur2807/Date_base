"""
В этом модуле лежит set представление.
"""

from django.shortcuts import render
from rest_framework import generics, viewsets
from files.models import UploadsFileModel
from .serializers import DataSerializers


class DataViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для действий над файлами.

    Полный CRUD для сущностей файлов.
    """
    queryset = UploadsFileModel.objects.all()
    serializer_class = DataSerializers

