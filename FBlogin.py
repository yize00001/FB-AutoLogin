from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--disable-notifications")

url = 'https://www.facebook.com/'
driver = webdriver.Chrome("/chromedriver.exe") 
#輸入使用者帳號密碼
useremail = '輸入email'
userpassword = '輸入密碼'

driver.get(url)
# 執行登入
enter_email = driver.find_element("id", "email")  # 輸入電子郵件
enter_email.send_keys(useremail)

enter_password = driver.find_element("id", "pass") # 輸入密碼
enter_password.send_keys(userpassword)

driver.find_element("name", "login").click() #按登入紐
time.sleep(5)
