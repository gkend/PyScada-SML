# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PyScadaSMLConfig(AppConfig):
    name = 'pyscada.sml'
    verbose_name = _("PyScada SML")
    path = os.path.dirname(os.path.realpath(__file__))
