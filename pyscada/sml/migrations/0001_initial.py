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
            name='ExtendedSmlDevice',
            fields=[
            ],
            options={
                'verbose_name': 'Sml Device',
                'verbose_name_plural': 'Sml Devices',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pyscada.device',),
        ),
        migrations.CreateModel(
            name='ExtendedSmlVariable',
            fields=[
            ],
            options={
                'verbose_name': 'Sml Variable',
                'verbose_name_plural': 'Sml Variables',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pyscada.variable',),
        ),
        migrations.CreateModel(
            name='SmlDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(blank=True, default='/dev/ttyUSB0', help_text='serial port', max_length=400)),
                ('baudrate', models.IntegerField(default=9600)),
                ('sml_device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pyscada.Device')),
            ],
        ),
    ]
