from django.contrib import admin

from .models import Sporsmen

@admin.register(Sporsmen)
class SportsmenAdmin(admin.ModelAdmin):
    #list_filter = ('name','last_name','birthday','weight','growth','male')
    list_display = [field.name for field in Sporsmen._meta.get_fields()]


# Register your models here.
