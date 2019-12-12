from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path = r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.co.uk/")
driver.maximize_window()

#CAPTURE ALL COOKIES created by the browser
cookies = driver.get_cookies()
# how many cookies are store in the browser
print(len(cookies))
#print cookies
print(cookies)

#ADD NEW COOKIES to the browser
cookies = {"name":"DanielCookie","value":"123456789"}
driver.add_cookie(cookies)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

#Deleting the cookies
driver.delete_cookie("DanielCookie")
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)









time.sleep(5)
driver.quit()