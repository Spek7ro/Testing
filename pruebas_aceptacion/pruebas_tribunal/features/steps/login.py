from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given(u'que ingreso a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@given(u'escribo  mi usuario "{usuario}" y mi contraseña "{password}"')
def step_impl(context, usuario, password):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(password)

@when(u'presiono el botón de Ingresar')
def step_impl(context):
    context.driver.find_element(By.ID, 'Ingresar').click()

@then(u'puedo ver mi usuario "{usuario}" en la barra principal')
def step_impl(context, usuario):
    div =  context.driver.find_element(By.PARTIAL_LINK_TEXT, usuario)
    print(div)
    time.sleep(3)
    assert div, f"El usuario {usuario} no se encuentra en {div}"

@then(u'puedo ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    div =  context.driver.find_element(By.ID, 'errordata')
    time.sleep(3)
    assert div.text, f"El mensaje  {mensaje} no se encuentra en {div.text}"
    