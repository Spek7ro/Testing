from behave import then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@then(u'debería ver a "{candidato}" como el candidato con más votos')
def step_impl(context, candidato):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.list-group-item'))
    )
    
    # Obtener todos los candidatos y sus votos
    candidatos = context.driver.find_elements(By.CSS_SELECTOR, '.list-group-item h5.mb-1')
    votos = context.driver.find_elements(By.CSS_SELECTOR, '.list-group-item small')
    
    # Convertir los votos a enteros y encontrar el máximo
    votos_numeros = [int(voto.text.split()[0]) for voto in votos]
    max_votos = max(votos_numeros)
    index_max_votos = votos_numeros.index(max_votos)
    
    # Verificar que el candidato con más votos coincida con el esperado
    candidato_con_max_votos = candidatos[index_max_votos].text
    assert candidato in candidato_con_max_votos, f"El nombre esperado '{candidato}' no coincide con el del candidato con más votos '{candidato_con_max_votos}'."
    time.sleep(3)
