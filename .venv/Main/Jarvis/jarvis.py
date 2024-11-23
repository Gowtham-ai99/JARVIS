from co_brain import Jarvis
import threading
from TTS_B import speak
from DATA.DLG_data import online_DLG
from DATA.DLG_data import offline_DLG
import random
from Automation.internet_check import is_Online
import time
from Automation.Alert import Alert
def main():

    random_online_msg = random.choice(online_DLG)
    random_offline_msg = random.choice(offline_DLG)
    if is_Online():
        
        t1= threading.Thread(target=Alert, args=(random_online_msg,))
        t2= threading.Thread(target=speak, args=(random_online_msg,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        time.sleep(1)
        Jarvis()
    else:
        Alert(random_offline_msg,)
        

main()
print ("Jarvis is ready sir!")


