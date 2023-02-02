from django.db import models


class Truck(models.Model):

    model = models.CharField(
        max_length=30,
        verbose_name='Модель грузовика',
    )
    number = models.CharField(
        max_length=10,
        verbose_name='Бортовой номер',
    )
    tonnage = models.IntegerField(
        verbose_name='Грузоподъёмность',
    )
    workload = models.IntegerField(
        default=0,
        verbose_name='Загруженность',
    )
    overload = models.FloatField(
        default=0,
        verbose_name='Перегрузка, %',
    )

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Самосвал'
        verbose_name_plural = 'Самосвалы'
        