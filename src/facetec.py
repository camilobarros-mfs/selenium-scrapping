import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


from src.constants import FACETEC_DASHBOARD, USERNAME, PASSWORD

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(FACETEC_DASHBOARD)
driver.find_element(By.ID, 'details-button').click()
driver.find_element(By.ID, 'proceed-link').click()

try:
    form = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "visible-md")))
    userInput = form.find_element(By.ID, 'signInFormUsername').send_keys(USERNAME)
    passwordInput = form.find_element(By.ID, 'signInFormPassword')
    passwordInput.send_keys(PASSWORD)
    passwordInput.send_keys(Keys.RETURN)

    driver.get(f'{FACETEC_DASHBOARD}photo-id-matches')

except:
    print("unable to login")
    driver.quit()

try:
    table = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "table-container")))
    # print(table.text)
    driver.find_element(By.ID, 'mat-select-0').click()
    driver.find_element(By.ID, 'mat-option-4').click()
    time.sleep(10)
    pagination = driver.find_element(By.CLASS_NAME, 'mat-paginator-range-label')
    # print(pagination.text)
    splitted_page = pagination.text.split()
    # print(splitted_page)
    register_displayed = splitted_page[2]
    total_register = splitted_page[4]
    total_pages = int(total_register)/int(register_displayed)
    it = int(total_pages)
    for p in range(it):
        time.sleep(10)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        next_page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,  "mat-paginator-navigation-next")))
        driver.execute_script("arguments[0].scrollIntoView();", next_page)
        next_page.click()
    time.sleep(5)

except:
    print("unable to parse the table")
    driver.quit()
