# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(verbose_name='Descrição', blank=True)),
                ('start_date', models.DateField(verbose_name='Data de início', null=True, blank=True)),
                ('image', models.ImageField(verbose_name='Imagem', upload_to='courses/images')),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
