from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=100)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return f"{self.name}"
    

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=250, blank=False, null=False, verbose_name="Modelo do Carro")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    factory_year = models.PositiveIntegerField(blank=False, null=False, verbose_name="Ano de Fabricação")
    model_year = models.PositiveIntegerField(verbose_name="Ano do Modelo")
    plate = models.CharField(max_length=10, blank=False, null=False, verbose_name="Placa do Carro")
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    photo = models.ImageField(upload_to="cars/")


    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    def __str__(self):
        return f"{self.model}"
    

class CarInvetory(models.Model):
    cars_count = models.IntegerField(verbose_name="Número de Carros")
    cars_value = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Valor total da Mercadoria")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Inventario de Carro"
        verbose_name_plural = "Inventario de Carros"

    def __str__(self):
        return f"{self.cars_count} - {self.cars_value}"