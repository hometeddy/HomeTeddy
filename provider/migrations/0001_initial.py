# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20150322_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=20)),
                ('desc', models.CharField(max_length=200)),
                ('ItemType', models.ForeignKey(to='service.ItemType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField(max_length=20)),
                ('item', models.ForeignKey(to='service.Item')),
                ('profile', models.ForeignKey(to='provider.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
