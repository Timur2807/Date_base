from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

def index(request):
    """Метод представляет личный кабинет пользователя."""
    username = request.user
    user = User.objects.get(username=username)
    context = {
        'user': user,
    }
    return render(request, 'account/index.html', context)


