from django.shortcuts import render
from .models import User
from menu.models import Sporsmen

def index(request):
    user = User.objects.all()
    sport = Sporsmen.objects.all()
    context = {
        'users': user,
        'sport': sport


    }
    
    return render(
        request,                # Запрос
        'mainpage/index.html',
        context,                 # подстановки


    )


def index2(request):
    user = User.objects.all()
    sport = Sporsmen.objects.all()
    context = {
        'users': user,
        'sport': sport


    }
    
    return render(
        request,                # Запрос
        'mainpage/index2.html',
        context,                 # подстановки

    )