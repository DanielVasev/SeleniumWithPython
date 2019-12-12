from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path= r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.co.uk/")
driver.maximize_window()

#Save ScreenShot
driver.save_screenshot(r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Python\TestMaterials\ScreenShots\homePage.png")

#Save as file
driver.get_screenshot_as_file(r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Python\TestMaterials\ScreenShots\homePage.png")

time.sleep(4)
driver.quit()