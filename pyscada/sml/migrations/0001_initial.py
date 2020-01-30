# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pyscada', '0036_auto_20170224_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedSMLDevice',
            fields=[
            ],
            options={
                'verbose_name': 'SML Device',
                'verbose_name_plural': 'SML Devices',
                'proxy': True,
                'indexes': [],
            },
            bases=('pyscada.device',),
        ),
        migrations.CreateModel(
            name='ExtendedSMLVariable',
            fields=[
            ],
            options={
                'verbose_name': 'SML Variable',
                'verbose_name_plural': 'SML Variables',
                'proxy': True,
                'indexes': [],
            },
            bases=('pyscada.variable',),
        ),
        migrations.CreateModel(
            name='SMLDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(blank=True, default='/dev/ttyUSB0', help_text='serial port', max_length=400)),
                ('baudrate', models.IntegerField(default=9600)),
                ('sml_device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pyscada.Device')),
            ],
        ),
    ]
