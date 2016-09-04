# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(db_index=True, max_length=45, choices=[(b'hospital', b'Hospital'), (b'walk_in_clinic', b'Walk in Clinic')])),
                ('name', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=45, blank=True)),
                ('postal_code', models.CharField(max_length=45, blank=True)),
                ('state', models.CharField(max_length=45, blank=True)),
                ('country', models.CharField(max_length=45, blank=True)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=7, db_index=True)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=7, db_index=True)),
                ('summary', models.TextField(blank=True)),
                ('phone_number', models.IntegerField(null=True, blank=True)),
                ('email', models.CharField(max_length=255, blank=True)),
                ('website', models.CharField(max_length=255, blank=True)),
                ('hours_of_operation', models.CharField(max_length=45)),
                ('rating', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('total_wait', models.IntegerField(default=0)),
            ],
        ),
    ]
