from django.contrib import admin
from .models import Conform

@admin.register(Conform)
class ConformAdmin(admin.ModelAdmin):
    list_display = ['name']