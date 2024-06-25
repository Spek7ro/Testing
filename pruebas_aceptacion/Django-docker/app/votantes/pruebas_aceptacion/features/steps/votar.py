from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given(u'hago clic en el botón Votar de "{candidato}"')
def step_impl(context, candidato):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/form/button').click()

@then(u'puedo ver "{n_votos}" votos para el candidato "{candidato}"')
def step_impl(context, candidato, n_votos):
    resultado = context.driver.find_element(By.XPATH, '/html/body/div/div/a[2]'.format(candidato))
    assert n_votos in resultado.text
    time.sleep(3)   