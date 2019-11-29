from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Video URl: https://www.youtube.com/watch?v=R67fOL27IGQ&list=PLUDwpEzHYYLvx6SuogA7Zhb_hZl3sln66&index=22



driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe", )

# creating class object
actions = ActionChains(driver)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#Find field "EnterData"
driver.find_element_by_css_selector('#textbox').send_keys('Hello Daniel')

# Wait for element
time.sleep(1)

# Click on "Generate File" button
generateBtn = driver.find_element_by_css_selector('#createTxt')
# Click on button "Generate File"
generateBtn.click()

# Wait for download btm
time.sleep(1)

# Click on download button
downloadBtn = driver.find_element_by_css_selector('#link-to-download')

#Click on download btn
downloadBtn.click()

time.sleep(5)
driver.quit()