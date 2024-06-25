class Calculadora:

    def sumar(self, num1, num2):
        if isinstance(num1, str) or isinstance(num2, str):
            return 'Solo se aceptan numeros'
        elif isinstance(num1, list) or isinstance(num2, list):
            return 'Solo acepto numeros no listas'
        elif not isinstance(num1, int) or not isinstance(num1, int):
            return 'Solo numeros enteros'
        elif num1 < 0 or num2 < 0:
            return 'Solo numeros positivos'
        else:
            return num1 + num2

    def restar(self, num1, num2):
        if isinstance(num1, str) or isinstance(num2, str):
            return 'Solo se aceptan numeros'
        elif isinstance(num1, list) or isinstance(num2, list):
            return 'Solo acepto numeros no listas'
        elif not isinstance(num1, int) or not isinstance(num1, int):
            return 'Solo numeros enteros'
        elif num1 < 0 or num2 < 0:
            return 'Solo numeros positivos'
        else:
            return num1 - num2

    def dividir(self, num1, num2):
        if isinstance(num1, str) or isinstance(num2, str):
            return 'Solo se aceptan numeros'
        elif isinstance(num1, list) or isinstance(num2, list):
            return 'Solo acepto numeros no listas'
        elif not isinstance(num1, int) or not isinstance(num1, int):
            return 'Solo numeros enteros'
        elif num1 < 0 or num2 < 0:
            return 'Solo numeros positivos'
        else:
            try:
                return num1 / num2
            except ZeroDivisionError:
                return 'No se puede dividir entre cero'

    def multiplicar(self, num1, num2):
        if isinstance(num1, str) or isinstance(num2, str):
            return 'Solo se aceptan numeros'
        elif isinstance(num1, list) or isinstance(num2, list):
            return 'Solo acepto numeros no listas'
        elif not isinstance(num1, int) or not isinstance(num1, int):
            return 'Solo numeros enteros'
        elif num1 < 0 or num2 < 0:
            return 'Solo numeros positivos'
        else:
            return num1 * num2

    def potencia(self, num1, num2):
        if isinstance(num1, str) or isinstance(num2, str):
            return 'Solo se aceptan numeros'
        elif isinstance(num1, list) or isinstance(num2, list):
            return 'Solo acepto numeros no listas'
        elif not isinstance(num1, int) or not isinstance(num1, int) and isinstance(num2, float):
            return 'Solo numeros enteros para la base, enteros o flotantes para el exponente'
        elif num1 < 0:
            return 'Solo numeros positivos para la base'
        else:
            return num1 ** num2
