from django.contrib import admin
from .models import Brand, Car, CarInvetory


class AdminBrand(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class AdminCar(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'plate', 'value')
    search_fields = ('model','factory_year', 'plate', 'value')

class CarInvetoryAdmin(admin.ModelAdmin):
    list_display = ('cars_count', 'cars_value', 'created_at')
    search_fields = ('cars_count', 'cars_value', 'created_at')

admin.site.register(Brand, AdminBrand)
admin.site.register(Car, AdminCar)
admin.site.register(CarInvetory, CarInvetoryAdmin)