# Register your models here.
from django.contrib import admin
from .models import Contact


class Admin(admin.ModelAdmin):
    pass

admin.site.register(Contact, Admin)
