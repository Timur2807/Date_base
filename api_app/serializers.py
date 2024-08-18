from rest_framework import serializers
from files.models import UploadsFileModel

class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model = UploadsFileModel
        fields = 'title', 'description', 'file', 'user'
