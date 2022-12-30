from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='name'),
    path('2', views.index2,)

]