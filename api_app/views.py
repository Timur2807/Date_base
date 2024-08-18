from django.shortcuts import render
from rest_framework import generics
from files.models import UploadsFileModel
from .serializers import DataSerializers
# Create your views here.
class DataAPIView(generics.ListAPIView):
    queryset = UploadsFileModel.objects.all()
    serializer_class = DataSerializers
