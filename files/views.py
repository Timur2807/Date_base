"""
В этом модуле представлены представления загрузки файлов.

И отображение загружаемых файлов.
"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import UploadsFileModel
from .forms import UploadsFileForms


# Create your views here.


def upload(request):
    if request.method == 'POST':
        form = UploadsFileForms(request.POST, request.FILES)
        if form.is_valid():
            newfile = form.save(commit=False)
            newfile.user = request.user
            newfile.save()

    else:
        form = UploadsFileForms()
    return render(request, 'files/my_files.html', {'form': form})


def file_list(request):
    files = UploadsFileModel.objects.filter(user=request.user)
    context = {
        'files': files,
    }
    return render(request, 'files/list_files.html', context)


def file_view(request, pk):
    file = get_object_or_404(UploadsFileModel, pk=pk, user=request.user)
    if request.method == 'GET':
        form = UploadsFileForms(instance=file)
        context = {
            'file': file,
            'form': form,
        }
        return render(request, 'files/detail_files.html', context)

