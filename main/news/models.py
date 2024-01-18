from django.db import models
# from PIL import Image


class publications(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'
