from django.contrib import admin
from .models import Fruit

class Fibre(admin.ModelAdmin):
    list_display = ('name','season','desc')


admin.site.register(Fruit,Fibre)


# Register your models here.
