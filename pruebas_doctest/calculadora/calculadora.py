# python -m doctest .\calculadora.py -v

class Calculadora:

    def sumar(self, num1, num2):
        if type(num1) == str or type(num2) == str:
            return 'Solo se aceptan numeros'
        elif type(num1) == list or type(num2) == list:
            return 'Solo acepto numeros no listas'
        elif type(num1) != int or type(num2) != int:
            return 'Solo numeros enteros'
        elif num1 < 0 or num2 < 0:
            return 'Solo numeros positivos'
        else:
            return num1 + num2
        
        
    def restar(self, num1, num2):
        if type(num1) == str or type(num2) == str:
            return 'Solo se aceptan numeros'
        elif type(num1) == list or type(num2) == list:
            return 'Solo acepto numeros no listas'
        elif type(num1) != int or type(num2) != int:
            return 'Solo numeros enteros'
        elif num1 < 0 or num2 < 0:
            return 'Solo numeros positivos'
        else:
            return num1 - num2

    def dividir(self, num1, num2):
        if type(num1) == str or type(num2) == str:
            return 'Solo se aceptan numeros'
        elif type(num1) == list or type(num2) == list:
            return 'Solo acepto numeros no listas'
        elif type(num1) != int or type(num2) != int:
            return 'Solo numeros enteros'
        elif num1 < 0 or num2 < 0:
            return 'Solo numeros positivos'
        else:
            try:
                return num1 / num2
            except ZeroDivisionError:
                return 'No se puede dividir entre cero'
 
    def multiplicar(self, num1, num2):
        if type(num1) == str or type(num2) == str:
            return 'Solo se aceptan numeros'
        elif type(num1) == list or type(num2) == list:
            return 'Solo acepto numeros no listas'
        elif type(num1) != int or type(num2) != int:
            return 'Solo numeros enteros'
        elif num1 < 0 or num2 < 0:
            return 'Solo numeros positivos'
        else:
            return num1 * num2

    def potencia(self, num1, num2):
        if type(num1) == str or type(num2) == str:
            return 'Solo se aceptan numeros'
        elif type(num1) == list or type(num2) == list:
            return 'Solo acepto numeros no listas'
        # Nota: Para potencia, aceptamos num2 como no entero porque la raíz cuadrada (1/2) es un caso común.
        elif type(num1) != int or (type(num2) != int and type(num2) != float):
            return 'Solo numeros enteros para la base, enteros o flotantes para el exponente'
        elif num1 < 0:
            return 'Solo numeros positivos para la base'
        else:
            return num1 ** num2
