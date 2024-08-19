from rest_framework import serializers
from files.models import UploadsFileModel

class DataSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UploadsFileModel
        fields = 'title', 'description', 'file', 'user'
