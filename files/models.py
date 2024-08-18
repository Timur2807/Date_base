from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UploadsFileModel(models.Model):
    title = models.CharField('Название файла', max_length=200)
    description = models.TextField('Описание',null=True, blank=True)
    file = models.FileField('Файл', upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
