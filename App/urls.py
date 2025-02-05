from django.urls import path
from .views import CarView, NewCarView



urlpatterns = [
    path("", CarView.as_view(), name='cars_list'),
    path("add_car", NewCarView.as_view(), name='add_car'),
]