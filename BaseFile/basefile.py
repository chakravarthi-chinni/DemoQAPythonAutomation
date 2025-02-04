from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import logging


class BaseFile:

    def __init__(self):
        # self.serv_path=Service("C:\\Users\\chakr\\Downloads\\BrowserDrivers\\chromedriver.exe")
        # self.driver=webdriver.Chrome(service=self.serv_path)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")

        try:
            chrome_driver_path = ChromeDriverManager().install()
            logging.info(f"ChromeDriver path: {chrome_driver_path}")  # Log the path
            service = Service(chrome_driver_path)
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            logging.info("ChromeDriver started successfully.") # Indicate success
            self.driver.get("https://demoqa.com/")
            self.driver.maximize_window()
            self.actions = ActionChains(self.driver)
        except Exception as e:
            logging.exception(f"Error during ChromeDriver setup: {e}") # Catch and log exceptions
            raise  # Re-raise the exception so the test fails

    def select_locator(self,value,locator):
        return self.driver.find_element(value,locator)

    def window_scroll(self,x_value,y_value):
        return self.driver.execute_script(f'window.scrollBy({x_value},{y_value})')

    def implicity_wait(self,time):
        return self.driver.implicitly_wait(time)

    def explicity_wait(self,time,value,locator):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located((value,locator)))

    def fluent_wait(self,time,value,locator):
        return WebDriverWait(self.driver,time,poll_frequency=0.2).until(EC.presence_of_element_located((value,locator)))
