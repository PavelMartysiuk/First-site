from django.db import models


# Create your models here.
class Bd(models.Model):

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-published']


    title = models.CharField(max_length=100, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True,blank = True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index= True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric',null = True,on_delete=models.PROTECT,verbose_name='Рубрика')

    def __str__(self):
        return self.title



class Rubric(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    def __str__(self):
        return self.name
    class Meta():
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
