from django.db import models


# Create your models here.

class Task(models.Model):
    status = models.BooleanField('status', default=False)
    title = models.CharField('title', max_length=25)
    descript = models.TextField('descript', max_length=70)
    when_created = models.DateTimeField(auto_now_add=True, db_index=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT)

    # 123l123l
    class Meta:
        verbose_name = 'задачу'
        verbose_name_plural = 'Задачи'

        ordering = ['title']

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


