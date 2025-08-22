import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_ACESS = Path(__file__).parent
CHROMEDRIVER_EXEC = os.path.join(ROOT_ACESS, 'driver', 'chromedriver.exe')

def chrome_maker(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROMEDRIVER_EXEC),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = chrome_maker(*options)

    # Como antes
    browser.get('https://www.google.com')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Hello World!')

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)