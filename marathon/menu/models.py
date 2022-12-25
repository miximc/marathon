from django.db import models

class Sporsmen(models.Model):
    name = models.CharField(default='Иванан', max_length=1024)
    last_name = models.CharField(default='Иванов', max_length=1024)
    father_name = models.CharField(default='Иванович', max_length=1024)
    birthday = models.DateTimeField()
    weight = models.IntegerField(default=170)
    growth = models.IntegerField(default=80)
    male = models.BooleanField(default=True)
    phone = models.IntegerField()


# Create your models here.
