# Register your models here.
from django.contrib import admin
from .models import Contact, ModelsLog


admin.site.register(Contact)
admin.site.register(ModelsLog)
