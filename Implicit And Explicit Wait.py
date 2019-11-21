from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # import time library
from selenium.webdriver.support import expected_conditions as EC # import time library
from selenium.webdriver.support.ui import WebDriverWait # import time library
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r"D:\STUDING\Python\WebDriver\chromedriver_win32\chromedriver.exe")



driver.implicitly_wait(10) # tova shte nakara stranicata da chaka zadadenoto vreme v sluchaq 10 sek i sled tova shte produlji s drugiq kod

driver.maximize_window() # maximise the browser window

driver.get("https://www.google.com/") # navigating to the page

driver.find_element_by_xpath("")


wait = WebDriverWait(driver,10) # izgrajdane na wait

element = wait.until(EC.element_to_be_clickable("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input"))


