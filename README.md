# Web Scrapping with Selenium

This project is a POC of how to extract data from the Facetec dashboard using selenium in python

1- Installing Selenium:
In order to automatize a browser and extract data from a website, selenium is required, to install it run the following command.
```
python -m pip install selenium
```
2- Configure a Webdriver
A Webdriver is required for you script to be able to initiate a web browser, you can install a webdriver from a service using the class webdriver as it's showed on the following code

```python
from selenium import webdriver

webdriver.Firefox
webdriver.FirefoxProfile
webdriver.Chrome
webdriver.ChromeOptions
webdriver.Ie
webdriver.Opera
webdriver.PhantomJS
webdriver.Remote
webdriver.DesiredCapabilities
webdriver.ActionChains
webdriver.TouchActions
webdriver.Proxy
```
In this particular case we are using Chrome as our browser, like this
 
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```
More info of the webdriver class can be found <a href="https://selenium-python.readthedocs.io/api.html" target="_blank">here</a>

3- With this you'll be able to use the method get from your driver to retreive any website

```python
driver.get('https://www.google.com/')
```
from now on your driver object will contain a copy of the full HTML code inside the requested website.

4- With this setup you can look and interact with any html element using the find_element as is showed on the following code

![img.png](img.png)
```html
<div id="inputWrapper">
    <input id="input" type="search" autocomplete="off" spellcheck="false" role="combobox" placeholder="Search Google or type a URL" aria-live="polite">
    <ntp-realbox-icon id="icon" in-searchbox="" background-image="" mask-image="search.svg">
    </ntp-realbox-icon>
        <button id="voiceSearchButton" title="Search by voice"></button>
    <ntp-realbox-dropdown id="matches" role="listbox" hidden=""></ntp-realbox-dropdown>
</div>
```
```python
search = driver.find_element(By.ID, 'input')
search.send_keys('any google search')
search.send_keys(Keys.RETURN)
```
more info about how to find an element using the method find_element can be found <a href="https://selenium-python.readthedocs.io/locating-elements.html#" target="_blank">here</a> 

5- Making sure than an element exist of if it is visible can be relevant for your script, because it won't be able to interact with element that aren't loaded or visibles yet.,
This is achievable using the expected conditions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```python
driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
```
more information of this topic can be found under the wait segments of the documentation <a href="https://selenium-python.readthedocs.io/waits.html" target="_blank">here</a> 