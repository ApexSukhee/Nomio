# Generated by Django 3.0.8 on 2020-08-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20200816_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='cart.CartItem'),
        ),
    ]
