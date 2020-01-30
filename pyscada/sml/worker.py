#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from pyscada.utils.scheduler import Process as BaseDAQProcess
from pyscada.models import BackgroundProcess
from pyscada.sml.models import SMLDevice
from pyscada.sml import PROTOCOL_ID


import json
import logging

logger = logging.getLogger(__name__)


class Process(BaseDAQProcess):
    def __init__(self, dt=5, **kwargs):
        super(Process, self).__init__(dt=dt, **kwargs)
        self.SML_PROCESSES = []

    def init_process(self):

        # clean up
        BackgroundProcess.objects.filter(parent_process__pk=self.process_id, done=False).delete()

        grouped_ids = {}
        for item in SMLDevice.objects.filter(sml_device__active=True):
            if item.protocol == PROTOCOL_ID:  # SML IP
                # every device gets its own process
                grouped_ids['%d-%s:%s-%d' % (item.sml_device.pk, item.ip_address, item.port, item.unit_id)] = [item]
                continue

            # every port gets its own process
            if item.port not in grouped_ids:
                grouped_ids[item.port] = []
            grouped_ids[item.port].append(item)

        for key, values in grouped_ids.items():
            bp = BackgroundProcess(label='pyscada.sml-%s' % key,
                                   message='waiting..',
                                   enabled=True,
                                   parent_process_id=self.process_id,
                                   process_class='pyscada.utils.scheduler.SingleDeviceDAQProcess',
                                   process_class_kwargs=json.dumps(
                                       {'device_ids': [i.sml_device.pk for i in values]}))
            bp.save()
            self.SML_PROCESSES.append({'id': bp.id,
                                          'key': key,
                                          'device_ids': [i.sml_device.pk for i in values],
                                          'failed': 0})

    def loop(self):
        """
        
        """
        # check if all sml processes are running
        for sml_process in self.SML_PROCESSES:
            try:
                BackgroundProcess.objects.get(pk=sml_process['id'])
            except BackgroundProcess.DoesNotExist or BackgroundProcess.MultipleObjectsReturned:
                # Process is dead, spawn new instance
                if sml_process['failed'] < 3:
                    bp = BackgroundProcess(label='pyscada.sml-%s' % sml_process['key'],
                                           message='waiting..',
                                           enabled=True,
                                           parent_process_id=self.process_id,
                                           process_class='pyscada.utils.scheduler.SingleDeviceDAQProcess',
                                           process_class_kwargs=json.dumps(
                                               {'device_ids': sml_process['device_ids']}))
                    bp.save()
                    sml_process['id'] = bp.id
                    sml_process['failed'] += 1
                else:
                    logger.debug('process pyscada.sml-%s failed more then 3 times' % sml_process['key'])

        return 1, None

    def cleanup(self):
        # todo cleanup
        pass
