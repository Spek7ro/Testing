from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://google.com") 

caja = driver.find_element(By.NAME, "q")

caja.send_keys("Ingeniero de software" + Keys.RETURN)
res = driver.find_element(By.ID, 'res')
items = res.find_elements(By.TAG_NAME, 'h3')

for item in items:
    if item.text != '':
        print(item.text)

time.sleep(10)
