from django.shortcuts import render
from .models import Sporsmen
def index(request):
    rows = Sporsmen.objects.all()
    context = {

        'salats':['Греческий',
                      'Цезарь',
                      'Капрезе',
                      'Крабовый'],
        'garnirs':['Паста',
                       'Рис',
                       'Овощи гриль',
                       'Картофель'],
        'sportsmen': rows
    }
    return render(
        request,                # Запрос
        'menu/index.html',# путь к шаблону
        context,                 # подстановки


    )
