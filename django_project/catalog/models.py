from django.db import models
from .validators import validate_amazing
from core.models import DefaultDBfields


class Category(DefaultDBfields):
    slug = models.SlugField(verbose_name='slug', max_length=200, unique=True)
    weight = models.PositiveSmallIntegerField(default=100, verbose_name='вес')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name[:15]


class Tag(DefaultDBfields):
    slug = models.SlugField(verbose_name='slug', max_length=200, unique=True)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name[:15]


class Item(DefaultDBfields):
    text = models.TextField(verbose_name='текст', help_text='Опишите объект',
                            validators=[validate_amazing('превосходно', 'роскошно', 'amazing',
                                                         'wonderful')])

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категории',
                                 related_name='items_category')

    tags = models.ManyToManyField(Tag, verbose_name='теги')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.text[:15]
