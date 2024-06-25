from behave import given, when, then
from fechaTexto import fechaTexto

@given('que el usuario ingresa la fecha "{fecha}"')
def step_impl(context, fecha):
    context.fecha = fecha

@when('se convierte la fecha a texto')
def step_impl(context):
    context.resultado = fechaTexto(context.fecha)

@then('el resultado debe ser "{esperado}"')
def step_impl(context, esperado):
    assert context.resultado == esperado, f"Esperado: {esperado}, Obtenido: {context.resultado}"
    