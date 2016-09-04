# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('waits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wait',
            name='location',
            field=models.ForeignKey(related_name='waits_for_location', to='locations.Location'),
        ),
        migrations.AlterField(
            model_name='wait',
            name='rating',
            field=models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='wait',
            name='user',
            field=models.ForeignKey(related_name='waits_for_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
