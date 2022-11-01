# Generated by Django 3.2.16 on 2022-11-01 14:11

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(help_text='max 150 символов', max_length=150,
                                          verbose_name='Название')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('weight', models.PositiveSmallIntegerField(default=100, verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(help_text='max 150 символов', max_length=150, verbose_name='Название')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(help_text='max 150 символов', max_length=150, verbose_name='Название')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('text', models.TextField(help_text='Опишите объект',
                                          validators=[catalog.validators.validate_amazing],
                                          verbose_name='Текст')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                               related_name='items_category', to='catalog.category')),
                ('tags', models.ManyToManyField(to='catalog.Tag')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
