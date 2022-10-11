import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.techwithtim.net/')
print(driver.title)

search = driver.find_element(By.NAME, 's')
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main")))
    # print(main.text)

    articles = main.find_elements(By.TAG_NAME, 'article')
    for article in articles:
        header = article.find_element(By.CLASS_NAME, 'entry-summary')
        print(header.text)

finally:
    driver.quit()
