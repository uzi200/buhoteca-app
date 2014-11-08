# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0004_auto_20141108_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='cover_url',
            field=models.ImageField(upload_to=b'covers', null=True, verbose_name=b'Cover', blank=True),
            preserve_default=True,
        ),
    ]
