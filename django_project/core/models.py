from django.db import models


class DefaultDBfields(models.Model):

    id = models.AutoField(primary_key=True, null=False, verbose_name='id')
    name = models.CharField(max_length=150, null=False, verbose_name='Название', help_text='max 150 символов')
    is_published = models.BooleanField(default=True, null=False, verbose_name='Опубликовано')

    class Meta:
        abstract = True
