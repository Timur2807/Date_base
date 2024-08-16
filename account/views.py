from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

def index(request):
    username = request.user
    user = User.objects.get(username=username)
    context = {
        'user': user,
    }
    return render(request, 'account/index.html', context)

def handle_uploaded_file(f):
    with open("uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def my_files(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file_upload'])
    return render(request, 'account/my_files.html')