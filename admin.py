from django.contrib import admin

# Register your models here.

from .models import Page, Nav

admin.site.register(Page)

admin.site.register(Nav)

