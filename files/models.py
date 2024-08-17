from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UploadsFileModel(models.Model):
    title = models.CharField('Название файла', max_length=200)
    file = models.FileField('Файл', upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
