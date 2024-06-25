from behave import given, when, then
from promedio import promedio

@given('que el usuario ingresa las calificaciones {calificaciones}')
def step_impl(context, calificaciones):
    context.calificaciones = eval(calificaciones)

@when('calculo el promedio')
def step_impl(context):
    context.resultado = promedio(*context.calificaciones)

@then('puedo ver el resultado igual a {esperado}')
def step_impl(context, esperado):
    # Convertir esperado a int para comparar correctamente con resultado
    assert context.resultado == int(esperado), f"Se esperaba {esperado}, pero se obtuvo {context.resultado}"

@then('puedo ver el mensaje: "{mensaje}"')
def step_impl(context, mensaje):
    assert str(context.resultado) == mensaje, f"Se esperaba el mensaje '{mensaje}', pero se obtuvo '{context.resultado}'"
