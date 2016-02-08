from django.contrib import admin

from .models import SavedRequest


class Admin(admin.ModelAdmin):
    pass

admin.site.register(SavedRequest, Admin)
