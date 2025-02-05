from django.shortcuts import render, redirect
from .models import Car, Brand
from .forms import BrandForm, CarForm
from django.views.generic import View

class CarView(View):
    
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)

        return render(request, 'cars.html', {'cars': cars})
    

class NewCarView(View):

    def get(self, request):
        new_car = CarForm()
        return render(request, 'new_car.html', {'new_car': new_car})
    
    def post(self, request):
        new_car = CarForm(request.POST, request.FILES)
        if new_car.is_valid():
            new_car.save()
            return redirect('cars_list')
        
        return render(request, 'new_car.html', {'new_car': new_car})
    