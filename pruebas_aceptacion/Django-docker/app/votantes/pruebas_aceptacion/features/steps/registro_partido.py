from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given(u'le doy clik en el enlace Partidos')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Partidos').click()

@given(u'luego clik en el boton de Agregar Partido')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="content-main"]/ul/li/a').click()

@given(u'escribo el nombre del partido "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)

@given(u'escribo la descripcion del partido "{descripcion}"')
def step_impl(context, descripcion):
    context.driver.find_element(By.NAME, 'descripcion').send_keys(descripcion)

@then(u'puedo ver el partido "{nombre}" en la lista de Partidos')
def step_impl(context, nombre):
    div =  context.driver.find_element(By.PARTIAL_LINK_TEXT, nombre)
    time.sleep(3)
    assert div.text, f"El {nombre} no se encuentra en {div.text}"
    time.sleep(1)
