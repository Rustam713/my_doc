from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

class SinglePod(models.Model):
    name = models.CharField(max_length=25)
    count_of_puffs = models.PositiveSmallIntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    images = models.ManyToManyField('SinglePod')

    def __str__(self):
        return self.name


class SinglePodImages(models.Model):
    file = models.ImageField(upload_to='mediafiles/single-pods/')


class Taste(models.Model):
    name = models.CharField(max_length=125)
    single_pod = models.ForeignKey(
        SinglePod,
        on_delete=models.PROTECT,
        related_name='tastes'
    )

    def __str__(self):
        return self.name


class SinglePodStock(models.Model):
    taste = models.ForeignKey(Taste, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

