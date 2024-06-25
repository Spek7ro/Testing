from behave import given, when, then
from calculadora import Calculadora

@given('el usuario ingresa los números "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)

@given('el usuario ingresa la cadena "{caracter}" y el número "{num2}"')
def step_impl(context, caracter, num2):
    context.num1 = caracter
    context.num2 = int(num2)

@given('el usuario ingresa la lista "{lista}" y el número "{num2}"')
def step_impl(context, lista, num2):
    context.num1 = eval(lista)
    context.num2 = int(num2)

@when('realizo la multiplicación')
def step_impl(context):
    cal = Calculadora()
    context.resultado = cal.multiplicar(context.num1, context.num2)

@then('puede el usuario ver el resultado igual a "{esperado}"')
def step_impl(context, esperado):
    assert str(context.resultado) == esperado, f"Se esperaba {esperado} pero fue {context.resultado}"

@then('puede el usuario ver el mensaje: "{mensaje}"')
def step_impl(context, mensaje):
    assert context.resultado == mensaje
