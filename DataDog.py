from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://login.microsoftonline.com/3f01317f-bda5-49d1-8668-9d3caae9970a/oauth2/authorize?client_id=0000000c-0000-0000-c000-000000000000&redirect_uri=https%3A%2F%2Faccount.activedirectory.windowsazure.com%2F&response_mode=form_post&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3D-jZ69-wkk6FfVlycvxC4A58c4q5b7bEuUOqlUE0U8GodSY715Gfbw9Q5b6tMnJPpEzellYSqoq_ftHGnwyK7MJ6EzCzUOcdvImGJoKVaXWkbq2-WbRbHUQ0moRarkw64LTNNwvq60HLxhlDQ3h1Z7eknVKwAwXIW3YI0b7bIdP3ChaM68ZgfrQV0jJZHxWrMaKNoDse2rHel3p8fd7-Qfu2gKwfxYVZvWYn57W3gti_FN3GFCxZpSXhInxznJlujFGGoEzFT4cjHHpFpkcuNTozkHg85qU5VXT-ibnwiCFbcwWuQM6El4WuZNYwQ0dmLqQCOmJcsaLSXX2sCtZUPuQ&nonce=1572860320.DQtXVMysI_XOV3eo3rGxWA&nux=1")
driver.maximize_window()

driver.implicitly_wait(3)

#User account
User = driver.find_element(By.CSS_SELECTOR,'#i0116').send_keys("daniel.vasev@boohoo.com")



#Click on Next Btn
NextBtn = driver.find_element(By.CSS_SELECTOR,'#idSIButton9').click()


#Insert password
Pass = driver.find_element(By.CSS_SELECTOR,'#i0118').send_keys("$Entinels8")

#Click Login CTA
title = driver.title
#Wait for element
time.sleep(1)
logInBtn = driver.find_element_by_css_selector('#idSIButton9').click()

#Confirm Yes button
time.sleep(1)
yesBtn = driver.find_element_by_css_selector('#idSIButton9').click()
#Click SignOut
time.sleep(2.5)
signOutBtn = driver.find_element_by_css_selector('#SignOutHyperLink').click()
#Choose account
time.sleep(3)
accountSelect = driver.find_element_by_css_selector('#tilesHolder > div.tile-container > div > div > div > div.table-cell.text-left.content > div').click()
#InserPass onece again
time.sleep(1)
Pass = driver.find_element(By.CSS_SELECTOR,'#i0118').send_keys("$Entinels8")
#Wait for element logIn btn
time.sleep(1)
logInBtn = driver.find_element_by_css_selector('#idSIButton9').click()
#Confirm Yes button
time.sleep(1)
yesBtn = driver.find_element_by_css_selector('#idSIButton9').click()
#DataDog icon click
time.sleep(3)

# DataDog Icon - driver.find_element_by_name('Datadog').click()
datadog = driver.find_element(By.XPATH,'//*[contains(@alt,"Datadog")]')
datadog.click()
time.sleep(5)

# click on logs

#Navigate to Logs search page.
logsBtn = driver.get('https://app.datadoghq.com/logs?cols=core_host%2Ccore_service&from_ts=1572952198257&index=main&live=true&messageDisplay=inline&stream_sort=desc&to_ts=1572953098257')
time.sleep(5)

driver.switch_to_window(driver.window_handles[1])

#click x button
#xBtn = driver.find_element_by_css_selector('#slide-1 > a > i').click()
xBtn = driver.find_element_by_css_selector('#slide-1 > a > i').click()

#Select Time drop down
#select=Select(driver.find_element_by_css_selector('#react-select-2--value-item > div > span.time-selector-row__description'))
select = Select(driver.find_element_by_xpath('//*[@class = "Select-control"]'))
select.click()
time.sleep(2)

select.select_by_visible_text('The Past 2 Days')

#driver.find_element_by_css_selector('#react-select-2--value-item > div > span.time-selector-row__description').send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)


time.sleep(2)

