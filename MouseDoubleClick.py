from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
print(driver.title)

actions = ActionChains(driver)

copyText = driver.find_element_by_css_selector('#HTML10 > div.widget-content > button')
actions.double_click(copyText).perform()


time.sleep(5)
driver.quit()

