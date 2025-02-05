from django.shortcuts import render, redirect
from .models import Car, Brand
from .forms import BrandForm, CarForm
from django.views.generic import ListView
from django.views.generic import CreateView

class CarsListview(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('value')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)

        return cars


class CarsCreateview(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = 'cars_list'

    
    