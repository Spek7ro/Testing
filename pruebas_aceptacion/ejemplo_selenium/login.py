from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from credenciales import correo, password

driver = webdriver.Chrome()

driver.get("https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&nonce=638482868327972449.f84b8ca5-1b5f-4b4b-b54f-11daed72904e&msaredir=1&client-request-id=e2856f15-a316-19b3-d372-6432ea4fcaf6&protectedtoken=true&claims=%7b%22id_token%22%3a%7b%22xms_cc%22%3a%7b%22values%22%3a%5b%22CP1%22%5d%7d%7d%7d&prompt=select_account&state=DYuxDoIwFABB_4UNLaVAOzQOJoZBjUEN6EL62pJIqJBSMf69He6muzAIgrVn5QmRV1DkKSUU05ymuGAFJoRtOkqASpHFCWRdTIBADBnp4iRRQqsCM0R06N9lO37FdjfZ0UyOz3rQ0rVCyvHzdpGQ7vp13NmPjmYnnOZJZLV6WR_dRi7KCsnylB9_bFFNNQNm9miYeZqhf16zHjBaoD5MsKftoz6je6rQpal-qr7_AQ&sso_reload=true") 

time.sleep(2)
driver.find_element(By.NAME, 'loginfmt').send_keys(correo +  Keys.RETURN)

time.sleep(2)
driver.find_element(By.NAME, 'passwd').send_keys(password +  Keys.RETURN)

time.sleep(2)
driver.find_element(By.ID, 'acceptButton').click()

# Vaciar carpeta de elemntos enviados
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="folderPaneDroppableContainer"]/div/div[1]/div[2]/div/div[2]/div/span').click()


# Eliminar spam
time.sleep(2)
spam_folder_xpath = ''
driver.find_element(By.XPATH, spam_folder_xpath).click()

# Lista de los correos enviados
time.sleep(2)
emails = driver.find_elements(By.XPATH, '//*[@id="folderPaneDroppableContainer"]/div/div[1]/div[2]/div/div[2]/div/span')  

for email in emails:
    print(email.text)  

time.sleep(10)
