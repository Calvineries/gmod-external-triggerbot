__author__ = 'github.com/Calvineries'

import pymem
import time
import pyautogui

#Memory
pm = pymem.Pymem('hl2.exe')
client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll

LocalPlayer = pm.read_uint(client + 0x007377A4)
LocalPlayerTarget = 0x3068
MaxOnlinePlayers = 0x4F4000

#TriggerBot
while 0 != 1:
    time.sleep(0.01)
    #If target player ID is less than max online player
    if pm.read_uint(LocalPlayer + LocalPlayerTarget) <= pm.read_uint(engine + MaxOnlinePlayers):
        #If target player ID is not 0
        if pm.read_uint(LocalPlayer + LocalPlayerTarget) != 0:
            pyautogui.leftClick()
