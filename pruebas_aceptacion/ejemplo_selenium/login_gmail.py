from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from credenciales import correo, password
import time

driver = webdriver.Chrome()

driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ARZ0qKKhypGwlB9TnCPmfAkXaVyEGNf7Tewcgr5VVktdg05agwdwUxtFGsQeolJC651TRcA4yD5B&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-703967227%3A1712957251082301&theme=mn&ddm=0")

# Ingresar el correo 
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, 'identifier'))
).send_keys(correo + Keys.RETURN)

# Ingresar la contraseña
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, 'Passwd'))
).send_keys(password + Keys.ENTER)

# Entrar a la opcion mail
element_to_hover_over = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div[3]/div/div[2]/div[1]/div[1]/div[1]"))
)

# Mover el cursor a la opcion mail
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()

# Entrar a la opcion mas
boton_mas = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, ":kd"))
)
ActionChains(driver).move_to_element(boton_mas).click().perform()

# Entar a la funcion papelera
papelera = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id=":kt"]/div/div[2]/span/a'))
)
papelera.click()

# Borrar papelera
empty_trash_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id=":mg"]/div[1]/span'))
)
empty_trash_button.click()

# Entar a la funcion spam
spam_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id=":ks"]/div/div[2]/span/a'))
)
spam_link.click()

time.sleep(5)