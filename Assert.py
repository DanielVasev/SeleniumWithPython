from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # import time library

driver = webdriver.Chrome(executable_path=r"D:\STUDING\Python\WebDriver\chromedriver_win32\chromedriver.exe")


driver.get("https://www.google.com/") # navigating to the page
driver.maximize_window() # maximise the browser window

print(driver.title)

assert "Google" in driver.title

