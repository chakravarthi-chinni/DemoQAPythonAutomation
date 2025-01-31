from selenium.webdriver.chrome.service import Service
from selenium import webdriver



from selenium import webdriver

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://demoqa.com")

# Get the title
title = driver.title.lower()
print("Page Title:", title)

# Close the browser
driver.quit()