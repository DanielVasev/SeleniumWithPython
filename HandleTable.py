from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://docs.oasis-open.org/dita/v1.0/langspec/simpletable.html")
driver.maximize_window()

# Find how many rows have the table
rows = len(driver.find_elements_by_css_selector('#simpletable__simpletable_attr > tbody > tr'))

# Find how many COLUMNS have the table
cols = len(driver.find_elements_by_css_selector('#simpletable__simpletable_attr > tbody > tr:nth-child(2) > td'))

print(rows)
print(cols)