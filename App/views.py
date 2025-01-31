from django.shortcuts import render, redirect
from .models import Car, Brand
from .forms import BrandForm, CarForm

def cars_view(request):
    search = request.GET.get('search')
    cars = Car.objects.all().order_by('model')

    if search:
        cars = Car.objects.filter(model__contains=search).order_by('model')
        

    return render(request, 'cars.html', {'cars': cars})


def new_car(request):
    if request.method == 'POST':
        new_car = CarForm(request.POST, request.FILES)

        if new_car.is_valid():
            new_car.save()
            return redirect('cars_list')

    else:
        new_car = CarForm()
    
    return render(request, 'new_car.html', {'new_car': new_car})