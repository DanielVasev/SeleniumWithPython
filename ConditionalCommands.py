from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # import time library

driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()

ele = driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input") # namira elementa koito iskame da rabotim nad nego

print(ele.is_displayed()) # izkarva suobshtenie dali e na ekrana dadeniq element

ele.send_keys("hello") # zadavane na tekst v search poleto 

print(ele.clear())



ele.is_enabled()