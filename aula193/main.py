import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_ACESS = Path(__file__).parent
CHROMEDRIVER_EXEC = os.path.join(ROOT_ACESS, 'driver', 'chromedriver.exe')

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=CHROMEDRIVER_EXEC)
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
)

chrome_browser.get('https://www.google.com/')
time.sleep(10)
