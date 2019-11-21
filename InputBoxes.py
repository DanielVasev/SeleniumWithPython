from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\daniel.vasev\Desktop\Boohoo\Lichna\Automation\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail&hl=en-GB&dsh=S352341316%3A1572262424669483&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
driver.maximize_window()

driver.implicitly_wait(3)

# locate field and insert name
driver.find_element(By.CSS_SELECTOR,'#firstName').send_keys("Das")

# locate field and insert lastName
driver.find_element(By.CSS_SELECTOR,'#lastName').send_keys("Bas")

