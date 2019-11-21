from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"D:\STUDING\Python\WebDriver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.com/")
driver.maximize_window()



# How many links present on the page.
links = driver.find_elements(By.TAG_NAME, 'a')
print("Number of links present on the page", len(links))


# Capture all links on the page.
for link in links:
    print(link.text)

# Click on the links

