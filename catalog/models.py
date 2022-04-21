from tabnanny import verbose
from django.db import models

class Goods(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    price = models.IntegerField('Цена')
    date = models.DateTimeField('Дата поставки')
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return f'/catalog/{self.pk}'
    

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
