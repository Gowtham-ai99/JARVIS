from NetHyTech_STT import listen
from Automation.Automation_Brain import automation_Brain
import threading
from os import getcwd


Recog_File = f"{getcwd()}\\input.txt"
def check_inputs():
    with open(Recog_File, 'w') as file:
        file.truncate(0)
    
    output_text = ""
    while True:
        with open(Recog_File, 'r') as file:
            input_text = file.read().lower()
        if input_text != output_text:
            output_text = input_text
            if output_text:
                automation_Brain(output_text)
                
        else:
            pass
   
def Jarvis():
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=check_inputs)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
