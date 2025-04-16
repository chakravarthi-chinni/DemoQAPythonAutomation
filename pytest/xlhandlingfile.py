from time import sleep

import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pytest.xmlutils import Utils
ser_path=Service("C:\\Users\\chakr\\Downloads\\BrowserDrivers\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_path)

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.execute_script("window.scrollBy(0,400)")

xl_path="C:\\Users\\chakr\\Desktop\\Book.xlsx"
row=Utils.get_rows(xl_path,"Sheet1")

for r in range(2,row+1):
    username=Utils.xl_read_data(xl_path,"Sheet1",r,1)
    password=Utils.xl_read_data(xl_path,"Sheet1",r,2)

    driver.find_element(By.XPATH,"//input[@id='username']").send_keys(username)
    sleep(4)
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password)
    sleep(4)
    driver.find_element(By.XPATH,"//button[text()='Submit']").click()
    text=driver.find_element(By.XPATH,"//h1[text()='Logged In Successfully']").text.lower()
    if text.__contains__("logged"):
        Utils.xl_write_data(xl_path,"Sheet1",r,3,"test passed")

