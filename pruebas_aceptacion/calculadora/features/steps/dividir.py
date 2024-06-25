from behave import given, when, then
from calculadora import Calculadora

@given(u'que el usuario ingresa los números "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    try:
        context.num1 = int(num1)
        context.num2 = int(num2)
    except:
        context.num1 = float(num1)
        context.num2 = float(num2)

@given(u'que el usuario ingresa la cadena "{caracter}" y el numero "{num2}"')
def step_impl(context, caracter, num2):
    context.num1 = caracter
    context.num2 = int(num2)

@given(u'que el usuario ingresa la lista "{lista}" y el numero "{num2}"')
def step_impl(context, lista, num2):
    context.num1 = eval(lista)
    context.num2 = int(num2)

@when(u'realizo la división')
def step_impl(context):
    num1 = context.num1
    num2 = context.num2
    cal = Calculadora()
    if not isinstance(num1, str) or not num1.isdigit():
        num1 = num1
    else:
        num1 = int(num1)
    if not isinstance(num2, str) or not num2.isdigit():
        num2 = num2
    else:
        num2 = int(num2)
    context.resultado = cal.dividir(num1, num2)

@then(u'puedo ver el resultado igual a "{esperado}"')
def step_impl(context, esperado):
    print(context.resultado)
    assert float(context.resultado) == float(esperado), f"{esperado} no es {context.resultado}" 

@then(u'puedo ver el mensaje: "{mensaje}"')
def step_impl(context, mensaje):
   assert context.resultado == mensaje

