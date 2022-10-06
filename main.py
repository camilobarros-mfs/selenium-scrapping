import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.techwithtim.net/')
print(driver.title)

search = driver.find_element(By.NAME, 's')
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
