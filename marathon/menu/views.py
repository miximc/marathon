from django.shortcuts import render

def index(request):
    context = {

        'salats':['Греческий',
                      'Цезарь',
                      'Капрезе',
                      'Крабовый'],
        'garnirs':['Паста',
                       'Рис',
                       'Овощи гриль',
                       'Картофель']
    }
    return render(
        request,                # Запрос
        'menu/index.html',# путь к шаблону
        context,                 # подстановки


    )
