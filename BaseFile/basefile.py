from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class BaseFile:

    def __init__(self):
        # self.serv_path=Service("C:\\Users\\chakr\\Downloads\\BrowserDrivers\\chromedriver.exe")
        # self.driver=webdriver.Chrome(service=self.serv_path)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")  # CRITICAL for CI
        chrome_options.add_argument("--disable-dev-shm-usage") # Also important
# Add any other options if needed (e.g., window size)
        # self.driver = webdriver.Chrome(options=chrome_options)
        # chrome_driver_path = ChromeDriverManager().install()
        # self.driver = webdriver.Chrome(service=Service(chrome_driver_path))
        chrome_driver_path = ChromeDriverManager().install()  # Install the driver
        service = Service(chrome_driver_path) # Create the service object
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        print(f"DEBUG: self.driver type -> {type(self.driver)}") 
        self.driver.get("https://demoqa.com/")
        self.driver.maximize_window()
        self.actions=ActionChains(self.driver)

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
