from django.db import models
from django.utils.safestring import mark_safe
from django.contrib import admin
from sorl.thumbnail import get_thumbnail
from .validators import validate_amazing
from core.models import DefaultDBfields
from tinymce.models import HTMLField


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


class Gallery(models.Model):
    image = models.ImageField(
        upload_to='uploads/',
        verbose_name='Изображение'
    )

    item = models.ForeignKey(
        verbose_name='Товар',
        to='Item',
        related_name='gallery',
        on_delete=models.CASCADE
    )

    @property
    def get_image(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(f'<img src="{self.get_image.url}">')
        return 'нет изображения'

    image_tmb.short_descriptions = 'превью изображения'
    image_tmb.allow_tags = True

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'изображение в галерее'
        verbose_name_plural = 'изображения в галерее'


class Item(DefaultDBfields):
    text = HTMLField(verbose_name='текст', help_text='Опишите объект. В описании обязательно '
                                                     'должны быть слова: роскошно, или превосходно, '
                                                     'или amazing, или wonderful',
                     validators=[validate_amazing('превосходно', 'роскошно', 'amazing',
                                                  'wonderful')])

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категории',
                                 related_name='items_category')

    tags = models.ManyToManyField(Tag, verbose_name='теги')

    upload = models.ImageField(default='', verbose_name='изображение', upload_to='upload/%Y/%m')

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.text[:15]


class Preview(models.Model):
    img = models.ImageField(upload_to='preview/%Y/%m', null=True, verbose_name="Изображение",
                            help_text="Загрузите картинку")
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True,
                                verbose_name="Товар", help_text="Выберите товар")

    def __str__(self):
        return self.img.url

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"
