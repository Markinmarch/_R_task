# Generated by Django 4.1.5 on 2023-02-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30, verbose_name='Модель грузовика')),
                ('number', models.CharField(max_length=10, verbose_name='Бортовой номер')),
                ('tonnage', models.IntegerField(verbose_name='Грузоподъёмность')),
                ('workload', models.IntegerField(default=0, verbose_name='Загруженность')),
                ('overload', models.FloatField(default=0, verbose_name='Перегрузка, %')),
            ],
            options={
                'verbose_name': 'Самосвал',
                'verbose_name_plural': 'Самосвалы',
            },
        ),
    ]
