from django.db.models.signals import pre_delete, pre_save, post_delete, post_save
from django.dispatch import receiver
from .models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print("### PRE SAVE ###")
    print(instance)

@receiver(post_save, sender=Car)
def post_save_car(sender, instance, **kwargs):
    print("## POST SAVE ##")
    print(instance)


@receiver(pre_delete, sender=Car)
def pre_delete_car(sender, instance, **kwargs):
    print("## PRE DELETE ##")
    print(instance)


@receiver(post_delete, sender=Car)
def post_delete_car(sender, instance, **kwargs):
    print("## POST DELETE @@")
    print(instance)
