# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0003_auto_20150322_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=200)),
                ('gender', models.CharField(default=b'G', max_length=2, choices=[(b'G', b'Gender'), (b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
                ('photo', models.CharField(max_length=200)),
                ('introduction', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('phone', models.IntegerField(max_length=20)),
                ('ItemType', models.ForeignKey(to='service.ItemType')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
