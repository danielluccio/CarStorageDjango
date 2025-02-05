from django.urls import path
from .views import CarsListview, CarsCreateview



urlpatterns = [
    path("", CarsListview.as_view(), name='cars_list'),
    path("add_car", CarsCreateview.as_view(), name='add_car'),
]