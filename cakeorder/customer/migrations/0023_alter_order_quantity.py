# Generated by Django 3.2.11 on 2023-07-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0022_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]