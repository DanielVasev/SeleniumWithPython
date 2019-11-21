from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"D:\STUDING\Python\WebDriver\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()

# click on button CLICK
driver.find_element_by_css_selector('#Tabbed > a > button').click()

handles = driver.window_handles
# find out tabs names
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

    # chossing which tab to close   
    if driver.title == 'Frames & windows':
        driver.close()



