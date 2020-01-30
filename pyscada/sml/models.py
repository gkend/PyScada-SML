# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.models import Variable, Device

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import logging

logger = logging.getLogger(__name__)


@python_2_unicode_compatible
class SmlVariable(models.Model):
    sml_variable = models.OneToOneField(Variable, on_delete=models.CASCADE)
    obis_code = models.CharField(default='', max_length=400, help_text='Obis Kennziffer: `1-0.1.8.0*255`')

    sensor_type_choices = (
            ('MT175', 'MT175'),
            ('Q3MA', 'Q3MA'),
        ) 
    
    sensor_type = models.CharField(default='', max_length=10, choices=sensor_type_choices)

    def __str__(self):
        return self.sml_variable.name


@python_2_unicode_compatible
class SmlDevice(models.Model):
    sml_device = models.OneToOneField(Device, on_delete=models.CASCADE)
    port = models.CharField(default='/dev/ttyUSB0',max_length=400, blank=True, help_text='serial port')
    device_id = models.CharField(max_length=400,blank=True, help_text='e.g. `1 ISK00 XXXXXXXX`') 
    baudrate= models.IntegerField(default=9600) 
    pin = models.IntegerField(null=True,blank=True,help_text='to get advanced data from device')

    def __str__(self):
        return self.sml_device.short_name


class ExtendedSmlDevice(Device):
    class Meta:
        proxy = True
        verbose_name = 'Sml Device'
        verbose_name_plural = 'Sml Devices'


class ExtendedSmlVariable(Variable):
    class Meta:
        proxy = True
        verbose_name = 'Sml Variable'
        verbose_name_plural = 'Sml Variables'

