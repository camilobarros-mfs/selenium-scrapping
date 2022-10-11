import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from src.constants import FACETEC_DASHBOARD, USERNAME, PASSWORD

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(FACETEC_DASHBOARD)
button = driver.find_element(By.ID, 'details-button')
button.click()
proceed = driver.find_element(By.ID, 'proceed-link')
proceed.click()
try:
    form = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "visible-md")))
    userInput = form.find_element(By.ID, 'signInFormUsername')
    userInput.send_keys(USERNAME)
    passwordInput = form.find_element(By.ID, 'signInFormPassword')
    passwordInput.send_keys(PASSWORD)
    passwordInput.send_keys(Keys.RETURN)

    driver.get(f'{FACETEC_DASHBOARD}photo-id-matches')

    time.sleep(10)
finally:
    print('end')
    # driver.quit()
