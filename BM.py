from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://development-bg1-boohoo.demandware.net/on/demandware.store/Sites-Site/default/ViewApplication-DisplayWelcomePage")
driver.maximize_window()

driver.implicitly_wait(3)

#User name
user = driver.find_element_by_css_selector('#idToken1').send_keys('daniel.vasev@boohoo.com')
#pass
passWord  = driver.find_element_by_css_selector('#idToken2').send_keys('$Entinels6')
# logIn
logIn = driver.find_element_by_css_selector('#loginButton_0').click()
time.sleep(4)

#Choose region
selectRegion = driver.find_element_by_css_selector('#SelectedSiteID-wrap > span')
selectRegion.click()
time.sleep(1)
selectSite = driver.find_element_by_css_selector('#SelectedSiteID-wrap > span > span.sod_list_wrapper > span > span.sod_option.active')
selectSite.click()
time.sleep(1)
selectCountry = driver.find_element_by_css_selector('#bm_content_column > table > tbody > tr > td > table > tbody > tr > td.top > table > tbody > tr:nth-child(4) > td > a')
selectCountry.click()
time.sleep(3)
#Select Merchant
merchTool = driver.find_element_by_css_selector('body.ext-safari.bm-welcome-page:nth-child(2) table.main:nth-child(9) header.header.header--Development:nth-child(9) div.header__wrapper div.header__navigation div.header__merchant-menu.bm-site-navigation-menus div.menu.bm-dropdown-menu.merchant-tools.active.show-menu:nth-child(1) span.menu-overview-link a.merchant-tools-link span.menu-overview-link-icon > span.icon-menu-menu_down_arrow')
merchTool.click()
time.sleep(0.5)
# Select Orders menue
orderMenu = driver.find_element_by_css_selector('table.main:nth-child(9) td.top td.top:nth-child(2) table.overview_item.orders tbody:nth-child(1) tr:nth-child(1) td.overview_subtitle > a.overview_subtitle:nth-child(2)').click()
# Select orders
time.sleep(0.5)
orderBtn = driver.find_element_by_css_selector('#bm_content_column > table > tbody > tr > td > table > tbody > tr > td.top > table > tbody > tr:nth-child(3) > td:nth-child(1) > table > tbody > tr:nth-child(1) > td.overview_subtitle > a').click()

