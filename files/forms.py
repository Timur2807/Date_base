from django import forms
from .models import UploadsFileModel


class UploadsFileForms(forms.ModelForm):
    class Meta:
        model = UploadsFileModel
        fields = 'title', 'file'

