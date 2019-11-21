from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # import time library

driver = webdriver.Chrome(executable_path=r"D:\STUDING\Python\WebDriver\chromedriver_win32\chromedriver.exe")


driver.get("https://www.google.com/") # navigating to the page
driver.maximize_window() # maximise the browser window

print(driver.title) # print page title

time.sleep(5) # wait for 5 sec beho carry on

print(driver.current_url) # print page URL




driver.close() # this can close the first opened page
driver.quit() # can close all of the pages opened by the test

