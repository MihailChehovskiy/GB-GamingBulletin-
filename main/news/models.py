from django.db import models
from django.urls import reverse
# from PIL import Image


class publications(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'


class News(models.Model):
    """Модель ноовсти"""
    title = models.CharField(max_length=200, verbose_name=('Title'))
    description = models.TextField(verbose_name=('Description'))
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('News')
        verbose_name_plural = ('News')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.pk)])
