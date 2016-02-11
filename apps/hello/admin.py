# Register your models here.
from django.contrib import admin
from .models import Contact, ModelsLog


class Admin(admin.ModelAdmin):
    pass

admin.site.register(Contact, Admin)
admin.site.register(ModelsLog, Admin)
