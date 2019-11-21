from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://us-dwdev.boohoo.com/")
driver.maximize_window()

# Should accept alert messahe
#driver.switch_to_alert().accept()

driver.switch_to_alert().dismiss()

