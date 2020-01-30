# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pyscada

__version__ = '0.1.0rc1'
__author__ = 'Gregor Kendzierski'
__email__ = 'gregor@kendzierski.de'
default_app_config = 'pyscada.sml.apps.PyScadaSMLConfig'

PROTOCOL_ID = 13

parent_process_list = [{'pk': PROTOCOL_ID,
                        'label': 'pyscada.sml',
                        'process_class': 'pyscada.sml.worker.Process',
                        'process_class_kwargs': '{"dt_set":30}',
                        'enabled': True}]
