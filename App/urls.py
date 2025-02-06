from django.urls import path
from .views import CarsListview, CarsCreateView, CarsDetailView, UpdateCarView, DeleteCarsView



urlpatterns = [
    path("", CarsListview.as_view(), name='cars_list'),
    path("add_car", CarsCreateView.as_view(), name='add_car'),
    path("<int:pk>", CarsDetailView.as_view(), name='detail_car'),
    path("update/<int:pk>", UpdateCarView.as_view(), name='update_car'),
    path('delete/<int:pk>', DeleteCarsView.as_view(), name='delete_car')
]