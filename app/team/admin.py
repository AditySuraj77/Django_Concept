from django.contrib import admin
from .models import Player

class Playerdetail(admin.ModelAdmin):
    list_display = ('name','age','detail')

admin.site.register(Player,Playerdetail)
# Register your models here.
