from django.contrib import admin
from .models import User

@admin.register(User)
class SportsmenAdmin(admin.ModelAdmin):
    #list_filter = ('name','last_name','birthday','weight','growth','male')
    list_display = [field.name for field in User._meta.get_fields()]

# Register your models here.
