from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"D:\STUDING\Python\WebDriver\chromedriver_win32\chromedriver.exe")

# creating class object
actions = ActionChains(driver)
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

# creting variables with locators for source element and target
sourceElem = driver.find_element_by_css_selector('#draggable > p')
target = driver.find_element_by_css_selector('#droppable')

time.sleep(3)

# perform drag and drop action


#actions.drag_and_drop(sourceElem,target).perform()
time.sleep(2)

actions.drag_and_drop(sourceElem,target).perform()


time.sleep(4)
driver.quit()
