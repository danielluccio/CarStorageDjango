from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=100, verbose_name="Nome da Marca")

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return f"Nome da Marca: {self.name}"
    

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=250, blank=False, null=False, verbose_name="Modelo do Carro")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    factory_year = models.PositiveIntegerField(blank=False, null=False, verbose_name="Ano de Fabricação")
    model_year = models.PositiveIntegerField(verbose_name="Ano do Modelo")
    plate = models.CharField(max_length=10, blank=False, null=False, verbose_name="Placa do Carro")
    value = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="cars/")


    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    def __str__(self):
        return f"Nome do Modelo: {self.model}"