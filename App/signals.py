from django.db.models.signals import post_delete, post_save, pre_save, pre_delete
from django.dispatch import receiver
from .models import Car, CarInvetory
from django.db.models import Sum

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInvetory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )


def car_inventory_delete():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInvetory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )




@receiver(post_save, sender=Car)
def post_save_car(sender, instance, **kwargs):
    car_inventory_update()
    

@receiver(post_delete, sender=Car)
def post_delete_car(sender, instance, **kwargs):
    car_inventory_update()


@receiver(pre_save, sender=Car)
def pre_save_car(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = ""


@receiver(pre_delete, sender=Car)
def pre_delete_car(sender, instance, **kwargs):
    pass
