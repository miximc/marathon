from django.db import models

class User(models.Model):
    Имя = models.CharField(default='Иванан', max_length=1024)
    Фамилия = models.CharField(default='Иванов', max_length=1024)
    Отчество = models.CharField(default='Иванович', max_length=1024)
    День_рождения = models.DateField()
    Рост = models.IntegerField(default=170)
    Вес = models.IntegerField(default=80)
    Пол = models.BooleanField(default=True)
    Телефон = models.IntegerField(default=11)
    Email = models.EmailField(default='',max_length=30)
    
