# Generated by Django 4.2 on 2023-04-22 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vendendor',
            new_name='Vendedor',
        ),
        migrations.AlterField(
            model_name='vendas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 22, 12, 5, 58, 103465)),
        ),
    ]