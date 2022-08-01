from django.contrib import admin
from .models import Qarzdorlar, Qarzdor

admin.site.register(Qarzdorlar, )

class AdminQarzdor(admin.ModelAdmin):
    list_display = ('qarzdorlar', 'product', 'date', 'price')

admin.site.register(Qarzdor, AdminQarzdor)