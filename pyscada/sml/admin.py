# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.gpio import PROTOCOL_ID
from pyscada.gpio.models import SMLDevice
from pyscada.gpio.models import SMLVariable
from pyscada.admin import DeviceAdmin
from pyscada.admin import VariableAdmin
from pyscada.admin import admin_site
from pyscada.models import Device, DeviceProtocol
from pyscada.models import Variable
from django.contrib import admin
import logging

logger = logging.getLogger(__name__)


class ExtendedSMLDevice(Device):
    class Meta:
        proxy = True
        verbose_name = 'SML Device'
        verbose_name_plural = 'SML Devices'


class SMLDeviceAdminInline(admin.StackedInline):
    model = SMLDevice


class SMLDeviceAdmin(DeviceAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'protocol':
            kwargs['queryset'] = DeviceProtocol.objects.filter(pk=PROTOCOL_ID)
            db_field.default = PROTOCOL_ID
        return super(SMLDeviceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(SMLDeviceAdmin, self).get_queryset(request)
        return qs.filter(protocol_id=PROTOCOL_ID)

    inlines = [
        SMLDeviceAdminInline
    ]


class ExtendedSMLVariable(Variable):
    class Meta:
        proxy = True
        verbose_name = 'SML Variable'
        verbose_name_plural = 'SML Variables'


class SMLVariableAdminInline(admin.StackedInline):
    model = SMLVariable


class SMLVariableAdmin(VariableAdmin):
    list_display = ('id', 'name', 'description', 'unit', 'device_name', 'value_class', 'active', 'writeable')
    list_editable = ('active', 'writeable',)
    list_display_links = ('name',)


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'device':
            kwargs['queryset'] = Device.objects.filter(protocol=PROTOCOL_ID)
        return super(SMLVariableAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(SMLVariableAdmin, self).get_queryset(request)
        return qs.filter(device__protocol_id=PROTOCOL_ID)

    inlines = [
        SMLVariableAdminInline
    ]


admin_site.register(ExtendedSMLDevice, SMLDeviceAdmin)
admin_site.register(ExtendedSMLVariable, SMLVariableAdmin)
