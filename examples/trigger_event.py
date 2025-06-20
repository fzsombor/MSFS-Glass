from ctypes import c_double
from ctypes.wintypes import DWORD

import logging
from time import sleep

from _ctypes import byref

from SimConnect import SimConnect
from SimConnect.Constants import SIMCONNECT_OBJECT_ID_USER_AIRCRAFT, SIMCONNECT_GROUP_PRIORITY_HIGHEST
from SimConnect.Enum import SIMCONNECT_EVENT_FLAG

logging.getLogger("SimConnect").setLevel(logging.DEBUG)

sm = SimConnect()

event_name= "COM2_RADIO_SET_HZ"

event = sm.map_to_sim_event(event_name)



sm.send_event(event, DWORD(124006000))

#sm.dll.TransmitClientEvent_EX1(sm.hSimConnect, SIMCONNECT_OBJECT_ID_USER_AIRCRAFT, event.value, SIMCONNECT_GROUP_PRIORITY_HIGHEST.value, SIMCONNECT_EVENT_FLAG.SIMCONNECT_EVENT_FLAG_GROUPID_IS_PRIORITY, DWORD(1),DWORD(1),DWORD(1),DWORD(1),DWORD(1))

while True:
    sleep(1)