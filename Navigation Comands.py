from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # import time library

driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input").send_keys("Hello") # can find search bar and will tape "Hello"

driver.find_element_by_css_selector("#lga").click() # click on some empty space in the page. 

driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.VlcLAe > center > input.gNO89b").click() # will find search button and will click on it

driver.back() # click on back browser button

driver.forward() # click on forward button

print(driver.title)

driver.close()


