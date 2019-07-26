from django.contrib import admin

# Register your models here.

from .models import person,skill

admin.site.register(person)
admin.site.register(skill)