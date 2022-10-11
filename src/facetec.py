import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://alb-dev-alb-face-dash-pa-433088894.us-east-1.elb.amazonaws.com/')
button = driver.find_element(By.ID, 'details-button')
button.click()
proceed = driver.find_element(By.ID, 'proceed-link')
proceed.click()
try:
    form = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "visible-md")))
    userInput = form.find_element(By.ID, 'signInFormUsername')
    userInput.send_keys('camilo.barros')
    passwordInput = form.find_element(By.ID, 'signInFormPassword')
    passwordInput.send_keys('Facetec.123')
    passwordInput.send_keys(Keys.RETURN)

    driver.get('https://alb-dev-alb-face-dash-pa-433088894.us-east-1.elb.amazonaws.com/photo-id-matches')

    time.sleep(10)
finally:
    print('end')
    # driver.quit()
