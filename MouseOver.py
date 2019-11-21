from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"D:\STUDING\Python\WebDriver\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")
driver.maximize_window()
driver.implicitly_wait(2000)
print(driver.title)

#creating "actions" class
actions = ActionChains(driver)

#Log in to the webSite
userName = driver.find_element_by_css_selector('#txtUsername').send_keys("admin")
userPass = driver.find_element_by_css_selector('#txtPassword').send_keys('admin123')
LoginBtn = driver.find_element_by_css_selector('#btnLogin').click()

#wait for element because the page is reloading
time.sleep(2)
print(driver.title)

# locate all of the element which we need to hover
admin = driver.find_element_by_css_selector('#menu_admin_viewAdminModule > b')
userManagment = driver.find_element_by_css_selector('#menu_admin_UserManagement')
users = driver.find_element_by_css_selector('#menu_admin_viewSystemUsers')

# execute action to hover element
actions.move_to_element(admin).move_to_element(userManagment).move_to_element(users).click().perform()
print(driver.title)

