from django.shortcuts import render, redirect
from .models import Car, Brand
from .forms import BrandForm, CarForm
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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



class CarsCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '../cars'



class CarsDetailView(DetailView):
    model = Car
    template_name = 'detail_car.html'


class UpdateCarView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'update_car.html'
    

    def get_success_url(self):
        return reverse_lazy('detail_car', kwargs={'pk': self.object.pk})


class DeleteCarsView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '../'

    
    