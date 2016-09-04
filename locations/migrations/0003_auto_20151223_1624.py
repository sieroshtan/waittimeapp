# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_location_number_of_wait_samples'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='phone_number',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='rating',
            field=models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
