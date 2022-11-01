from django.db import models
from .validators import validate_amazing
from core.models import DefaultDBfields


class Category(DefaultDBfields):
    slug = models.SlugField(verbose_name='slug', max_length=200, unique=True)
    weight = models.PositiveSmallIntegerField(default=100, verbose_name='Вес')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.slug[:15]


class Tag(DefaultDBfields):
    slug = models.SlugField(verbose_name='slug', max_length=200, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.slug[:15]


class Item(DefaultDBfields):
    text = models.TextField(verbose_name='Текст', help_text='Опишите объект', validators=[validate_amazing])

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категории', related_name='items_category')

    tags = models.ManyToManyField(Tag, verbose_name='теги')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.text[:15]
