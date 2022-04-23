from django.contrib import admin
from .models import *


class ClinicAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Direction)
admin.site.register(Clinic, ClinicAdmin)
