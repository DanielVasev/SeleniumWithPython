from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.toolsqa.com/iframe-practice-page/")
driver.maximize_window()
time.sleep(2)
cookies = driver.find_element_by_css_selector('#cookie_action_close_header').click()
time.sleep(2)


# go to first frame
driver.switch_to.frame("iframe1")
time.sleep(2)

# select element from Iframe 1
elemOne = driver.find_element_by_css_selector('#primary-menu > li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-has-children.menu-item-26284.has-children > ul > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-27307 > a > span > span')
print(elemOne.is_displayed())
time.sleep(2)

#Move back to main frame
driver.switch_to.default_content()
time.sleep(2)



# find input field over "Subscribe" btn
emailField = driver.find_element_by_css_selector('#text-10 > div.textwidget > form > p:nth-child(2) > input[type=text]')
emailField.send_keys('Hello Daniel')



