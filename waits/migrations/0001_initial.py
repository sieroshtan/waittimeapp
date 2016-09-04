# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wait',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('star_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('total_time', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('rating', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('rating_comment', models.CharField(max_length=1000, blank=True)),
                ('location', models.ForeignKey(related_name='locations', to='locations.Location')),
                ('user', models.ForeignKey(related_name='waits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
