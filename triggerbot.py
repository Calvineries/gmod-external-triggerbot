import pymem
import time
import pyautogui

#Memory
pm = pymem.Pymem('hl2.exe')
client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
OffLocalPlayer = pm.read_uint(client + 0x007377A4)

#TriggerBot
while 0 != 1:
    time.sleep(0.01)
    #If target player ID is less than online player counts
    if pm.read_uint(OffLocalPlayer + 0x3068) <= pm.read_uint(engine + 0x4F4000):
        #If target player ID is not 0
        if pm.read_uint(OffLocalPlayer + 0x3068) != 0:
            pyautogui.leftClick()

