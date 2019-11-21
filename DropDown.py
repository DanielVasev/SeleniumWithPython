from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.implicitly_wait(3)


dropDownSkills = driver.find_element(By.CSS_SELECTOR,'#Skills')
dropDownSkills.click()
# selecting drop down
drp = Select(dropDownSkills)


# selecting element in the drop down by text
drp.select_by_visible_text("CSS")

dropDownCountry = driver.find_element(By.CSS_SELECTOR, '#countries')
dropDownCountry.click()
drpCountry = Select(dropDownCountry)

# select drop down element by text
# drpCountry.select_by_visible_text('Bahrain')


# select drop down element by value
drpCountry.select_by_value('Bangladesh')

# selecting element in the drop down by INDEX if is available IN THIS CASE IS NOT.
#   drp.select_by_index()

# count number of elements in the drop down
print(len(drp.options))
