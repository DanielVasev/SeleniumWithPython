from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

driver.implicitly_wait(3)

selector = driver.find_element(By.CSS_SELECTOR, '#checkbox2')

print(selector.is_displayed())
print(selector.is_enabled())
print(selector.is_selected())

selector.click()

print(selector.is_selected())