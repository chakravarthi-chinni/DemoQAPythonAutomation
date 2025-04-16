# https://clario.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


class Basefileclario:
    def __init__(self):
        self.servpath=Service("C:\\Users\\chakr\\\Downloads\\BrowserDrivers\\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.servpath)
        self.driver.get("https://clario.com/")
        self.driver.maximize_window()
    def select_loactor(self,locator,attribute):
        return self.driver.find_element(locator,attribute)
    def window_scroll(self,x_path,y_path):
        return self.driver.execute_script(f'window.scrollBy({x_path},{y_path})')
    def implicit_wait(self,time):
        return self.driver.implicitly_wait(time)
    def explicit_wait(self,time,locator,attribute):
        return WebDriverWait(self.driver,time).until(Ec.presence_of_element_located((locator,attribute)))
    def fluent_wait(self,time,locator,attribute):
        return WebDriverWait(self.driver,time,poll_frequency=0.2).until(Ec.presence_of_element_located((locator,attribute)))
