"""
В этом модуле представлены представления загрузки файлов.

И отображение загружаемых файлов.
"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import UploadsFileModel
from .forms import UploadsFileForms


# Create your views here.

def handle_uploaded_file(f):
    with open(f"media/uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def uploads(request):
    """Метод обрабатывает запрос загрузки файла от пользователя."""
    if request.method == 'POST':
        form = UploadsFileForms(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
            newfile = form.save(commit=False)
            newfile.user = request.user
            newfile.save()
            return redirect('files:file_list')
    else:
        form = UploadsFileForms()
    return render(request, 'files/my_files.html', {'form': form})


def file_list(request):
    """Метод представляет список загруженных файлов."""
    files = UploadsFileModel.objects.filter(user=request.user)
    context = {
        'files': files,
    }
    return render(request, 'files/list_files.html', context)


def file_view(request, pk):
    """Метод представляет информацию о файле."""
    file = get_object_or_404(UploadsFileModel, pk=pk, user=request.user)
    if request.method == 'GET':
        form = UploadsFileForms(instance=file)
        context = {
            'file': file,
            'form': form,
        }
        return render(request, 'files/detail_files.html', context)

