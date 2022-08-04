from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("E:/OneDrive - 朝陽科技大學/PYTHON自學/New python/數據資料爬取/自動登入/chromedriver.exe") 


driver.get("https://www.dcard.tw/f")
# search = driver.find_element("name", "query")
# search.send_keys("比特幣")
# search.send_keys(Keys.RETURN)
titles = driver.find_elements(By.CLASS_NAME, "sc-8fe4d6a1-3")
for title in titles:
    print(title.text)

time.sleep(5)
# driver.quit()