# Generated by Django 5.1.5 on 2025-01-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0002_alter_car_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="value",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
