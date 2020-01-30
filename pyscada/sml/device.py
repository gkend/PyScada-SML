# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import time 
from serial import Serial
from sml import SmlBase
import logging

logger = logging.getLogger(__name__)

OBIS_DEVICE_ID = '1-0:0.0.9*255' 

class Device:
    def __init__(self, device):
        self.variables = []
        self.device = device
        self.instr = Serial(
            port = self.device.smldevice.port, 
            baudrate = self.device.smldevice.baudrate
        )
        self.device_id = self.device.smldevice.device_id

        for var in device.variable_set.filter(active=1):
            if not hasattr(var, 'smlvariable'):
                continue
            self.variables.append(var)

    def request_data(self):
        """

        """
        trys = 50
        while trys > 0:
            timestamp = time()
            out = SmlBase.parse_frame(self.instr.read(912)) 
            if len(out) == 2: 
               frameId, frame = out 
               break 
            else:
                trys -= 1
                logger.debug('[%s]Reading again try: %d' %(self.device_id, 50-trys))
            
        if trys == 0: 
            return []

        msg = [ msg['messageBody'] for msg in frame if 'messageBody' in msg ]
        objNames = [ item['valList'] for item in msg if 'valList' in item][0]

        device_id =  [ obj['value'] for obj in objNames if obj['objName']  == OBIS_DEVICE_ID ][0]
        
        if device_id != self.device_id:
            logger.debug('Wrong Device Connected: %s, expected: %s' %(device_id,self.device_id)) 
         
        output = []
        #logger.debug(self.variables)
        for item in self.variables: 
            obis_code = item.smlvariable.obis_code 
            # logger.debug([obis_code, [ obj['objName'] for obj in objNames] ] )
            value = [ obj['value'] for obj in objNames if obj['objName'] == obis_code]
            
            if len(value) < 1: 
                value = None
            
            # logger.debug(value[0])
            # update variable
            if value is not None and item.update_value(value[0], timestamp):
                output.append(item.create_recorded_data_element())
        
        return output

