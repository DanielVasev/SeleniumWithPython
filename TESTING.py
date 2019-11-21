from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"D:\STUDING\Python\WebDriver\chromedriver_win32\chromedriver.exe")

driver.get("https://uk-dwdev.boohoo.com/")
driver.maximize_window()

#Closing the pop up
closingPopUp = driver.find_element_by_css_selector('#dialog-container > div > div.welcome-popup-content-col > div.welcome-popup-btn-inner.hidden-on-mobile > a:nth-child(1) > span').click()




#Scrolling to the bottom
#driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

