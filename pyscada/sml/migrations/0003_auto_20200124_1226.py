# Generated by Django 2.2.9 on 2020-01-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sml', '0002_add_protocol_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smlvariable',
            name='address',
        ),
        migrations.AddField(
            model_name='smldevice',
            name='device_id',
            field=models.CharField(blank=True, help_text='e.g. `1 ISK00 XXXXXXXX`', max_length=400),
        ),
        migrations.AddField(
            model_name='smldevice',
            name='pin',
            field=models.IntegerField(blank=True, default=None, help_text='to get advanced data from device'),
        ),
        migrations.AddField(
            model_name='smlvariable',
            name='obis_code',
            field=models.CharField(default='', help_text='Obis Kennziffer: `1-0.1.8.0*255`', max_length=400),
        ),
        migrations.AlterField(
            model_name='smlvariable',
            name='sensor_type',
            field=models.CharField(choices=[('MT175', 'MT175 Elektronischer EDL-Dreiphasen-Wirkverbrauchzähler'), ('Q3MA', 'Q3MA Elektronischer Haushaltszähler')], default='', max_length=10),
        ),
    ]