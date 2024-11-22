import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

logging.getLogger('selenium').setLevel(logging.WARNING)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")


chrome_service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chrome_service,options = chrome_options)



driver.get("https://tts.5e7en.me/")
time.sleep(2)

def Speak(text):
    try:
        element_to_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')))
        element_to_click.click()
        
        element_to_click.send_keys(text)
        print (text)

        if len(text) < 15:
            sleep_duration  = min(0.5+len(text)//4,5)

        else:
            sleep_duration = min(0.2+len(text)//7,7)
        
        button_to_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]')))
        print("Clicking the play button for TTS")
        button_to_click.click()

        driver.save_screenshot("screenshot.png")

        time.sleep(sleep_duration)
        print("Audio Should be playing now...")
         
        element_to_click.clear()

    except Exception as e:
        print(f"An error occurred: {e}")

Speak ("Hey")
Speak ("Hi")
Speak ("I am your personal assistant and I am created by Mister T Gowtham Venkat Raj Kumar")
Speak ("thank you")
