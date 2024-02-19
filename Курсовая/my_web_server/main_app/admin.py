from django.contrib import admin
from .models import *

@admin.register(Tasks)
class Tasks(admin.ModelAdmin):
    list_display = ['id', 'title', ]



