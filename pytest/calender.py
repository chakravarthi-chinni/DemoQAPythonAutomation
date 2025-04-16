import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_path=Service("C:\\Users\\chakr\\Downloads\\BrowserDrivers\\chromedriver.exe")

driver=webdriver.Chrome(service=serv_path)

driver.get("https://www.tutorialspoint.com/selenium/practice/date-picker.php")
driver.execute_script("window.scrollBy(0,100)")
driver.find_element(By.XPATH,"//a[text()=' Date Picker']").click()
time.sleep(4)
driver.execute_script("window.scrollBy(0,100)")
driver.find_element(By.XPATH,"//input[@id='datetimepicker1']").click()
driver.execute_script("window.scrollBy(0,170)")

# select_date.()

