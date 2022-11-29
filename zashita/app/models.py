from django.db import models

class News(models.Model):
    title = models.CharField(max_length=222)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/%Y/%m/%d')
    content = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} {self.created} {self.image} {self.content}"


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новость'
        ordering = ['-id', ]