# Generated by Django 3.2.11 on 2023-07-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
