import psutil
import time
from win10toast import ToastNotifier
from TTS_B import speak
import threading 
from Alert import Alert

def Battery_Alert():
    while True:
        battery = psutil.sensors_battery()
        percentage = int(battery.percent)
        time.sleep(30)
        if percentage <= 50:
            t1 = threading.Thread(target=Alert, args=(f"The battery is below 50% , Please Plug it"))
            t2 = threading.Thread(target=speak, args=(f"Sir sorry to disturb You,you have {percentage} battery,please plug the charger"))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        if percentage <= 40:
            t1 = threading.Thread(target=Alert, args=(f"The battery is below 40% , Please Plug it"))
            t2 = threading.Thread(target=speak, args=(f"Sir sorry to disturb You,you have {percentage} battery,please plug the charger we dont have much battery left"))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        if percentage <= 30:
            t1 = threading.Thread(target=Alert, args=(f"The battery is below 30% , Please Plug it"))
            t2 = threading.Thread(target=speak, args=(f"Sir sorry to disturb You,you have {percentage} battery,please plug the charger immediately"))
            t1.start()
            t2.start()
            t1.join()
            t2.join()