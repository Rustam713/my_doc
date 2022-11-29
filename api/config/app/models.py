from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Car(models.Model):
    vim = models.CharField(verbose_name='VIM',
                           db_index=True,
                           max_length=222)
    name = models.CharField(max_length=222)
    color = models.CharField(max_length=222)
    TYPE = (
        (1, 'Sedan'),
        (2, 'Crosover'),
        (3, 'Universal'),
        (4, 'Cupe'),
    )
    car_type = models.IntegerField(verbose_name='Car type',
                                   choices=TYPE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

