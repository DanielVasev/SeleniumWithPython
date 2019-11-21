from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"D:\STUDING\Python\WebDriver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#driver.find_element_by_css_selector('#dialog-container > div > div.welcome-popup-content-col > div.welcome-popup-btn-inner.hidden-on-mobile > a:nth-child(1) > span').click()

time.sleep(3)

# scroll down by pixels
#driver.execute_script("window.scrollBy(0,1000)", " ")


# scroll down to element on the page
#flag = driver.find_element_by_css_selector('#content > div.container > div:nth-child(2) > table:nth-child(1) > tbody > tr:nth-child(82) > td:nth-child(1) > img')
#driver.execute_script("arguments[0].scrollIntoView();", flag)

# scroll down to the bottom of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
