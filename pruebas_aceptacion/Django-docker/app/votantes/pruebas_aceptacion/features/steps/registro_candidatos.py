from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given(u'presiono el botón de Ingresar')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()

@given(u'le doy clik en el enlace Candidatos')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Candidatos').click()

@given(u'luego clik en el boton de Agregar candidato')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="content-main"]/ul/li/a').click()

@given(u'escribo el nombre del candidato "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)

@given(u'escribo el apellido paterno del candidato "{ap_paterno}"')
def step_impl(context, ap_paterno):
    context.driver.find_element(By.NAME, 'aPaterno').send_keys(ap_paterno)

@given(u'escribo el apellido materno del candidato "{ap_materno}"')
def step_impl(context, ap_materno):
    context.driver.find_element(By.NAME, 'aMaterno').send_keys(ap_materno)

@given(u'selecciono la imagen del candidato "{path_imagen}"')
def step_impl(context, path_imagen):
    context.driver.find_element(By.NAME, 'foto').send_keys(path_imagen)

@given(u'selecciono el partido "{partido}"')
def step_impl(context, partido):
    context.driver.find_element(By.NAME, 'Partido').send_keys(partido)

@when(u'presiono el boton Guardar')
def step_impl(context):
    context.driver.find_element(By.NAME, '_save').click()

@then(u'puedo ver el candidato "{nombre}" en la lista de candidatos')
def step_impl(context, nombre):
    div =  context.driver.find_element(By.PARTIAL_LINK_TEXT, nombre)
    time.sleep(3)
    assert div.text, f"El {nombre} no se encuentra en {div.text}"
    time.sleep(1)
    