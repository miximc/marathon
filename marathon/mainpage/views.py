from django.shortcuts import render

def index(request):
    context = {
        'nomer_okowko': 25,
        'phone': 2}
    return render(
        request,                # Запрос
        'mainpage/index.html',  # путь к шаблону
        context                 # подстановки
    )
    # Create your views here.
