from django.shortcuts import render
from .models import User
def index(request):
    user = User.objects.all()
    context = {
        'users': user

    }
    

    return render(
        request,                # Запрос
        'mainpage/index.html',
        context,                 # подстановки


    )


