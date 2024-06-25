from behave import given, when, then
from calculadora import Calculadora

@given(u'que el usuario ingresa los numeros "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)

@given(u'que el usuario ingresa el caracter "{caracter}" y el numero "{num2}"')
def step_impl(context, caracter, num2):
    context.num1 = caracter
    context.num2 = int(num2)

@when(u'realizo el calculo de sumar')
def step_impl(context):
    cal = Calculadora()
    context.resultado = cal.sumar(context.num1, context.num2)   

@then(u'poder ver el resultado igual a "{esperado}" de la suma')
def step_impl(context, esperado):
    assert context.resultado == int(esperado), f"{esperado} no es {context.resultado}" 

@then(u'puede ver el mensaje: "{mensaje}"')
def step_impl(context, mensaje):
    assert context.resultado == mensaje, f"{mensaje} no es {context.resultado}"
    
