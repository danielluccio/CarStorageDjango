from django.urls import path
from .views import cars_view, new_car



urlpatterns = [
    path("", cars_view, name='cars_list'),
    path("add_car", new_car, name='add_car'),
]