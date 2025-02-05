from django.urls import path
from .views import CarsListview, CarsCreateview, CarsDetailView, UpdateCarView



urlpatterns = [
    path("", CarsListview.as_view(), name='cars_list'),
    path("add_car", CarsCreateview.as_view(), name='add_car'),
    path("<int:pk>", CarsDetailView.as_view(), name='detail_car'),
    path("update/<int:pk>", UpdateCarView.as_view(), name='update_car')
]