from django.contrib import admin
from .models import Brand, Car


class AdminBrand(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class AdminCar(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'plate', 'value')
    search_fields = ('model','factory_year', 'plate', 'value')


admin.site.register(Brand, AdminBrand)
admin.site.register(Car, AdminCar)