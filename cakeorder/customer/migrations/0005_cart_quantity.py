# Generated by Django 3.2.11 on 2023-07-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
