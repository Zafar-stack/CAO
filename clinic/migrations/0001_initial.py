# -*- coding: utf-8 -*-
# Generated by Django 1.9.dev20150914174135 on 2015-09-14 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название клиники')),
                ('title2', models.CharField(max_length=200, verbose_name='ENG название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Загрузить фото')),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название клиники')),
            ],
        ),
        migrations.AddField(
            model_name='clinic',
            name='directions',
            field=models.ManyToManyField(to='clinic.Direction', verbose_name='направления'),
        ),
    ]