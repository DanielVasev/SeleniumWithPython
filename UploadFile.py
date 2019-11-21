from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"D:\STUDING\Python\WebDriver\chromedriver_win32\chromedriver.exe")


driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame(0)

driver.find_element_by_css_selector()