from django.contrib import admin
from .models import Character

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "species", "char_class", "level", )
    date_hierarchy = "created_on"
