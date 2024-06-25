import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    # Instancia el objeto calculadora para las pruebas
    def setUp(self):
        self.calc = Calculadora()

    # Pruebas unitarias para la funcion de sumar 
    def test_sumar_dos_mas_dos(self):
        resultado = self.calc.sumar(2, 2)
        self.assertEqual(4, resultado)

    def test_sumar_cadena(self):
        resultado = self.calc.sumar('x', 2)
        self.assertEqual('Solo se aceptan numeros', resultado) 

    def test_sumar_num_positivos(self):
        resultado = self.calc.sumar(-4, 5)
        self.assertEqual('Solo numeros positivos', resultado)                

    def test_sumar_num_enteros(self):
        resultado = self.calc.sumar(9.5, 5.2)
        self.assertEqual('Solo numeros enteros', resultado)   

    def test_sumar_no_listas(self):
        resultado = self.calc.sumar([3,4,5], 2)
        self.assertEqual('Solo acepto numeros no listas', resultado) 

    # Pruebas unitarias para la funcion de restar 
    def test_retar_diez_menos_cinco(self):
        resultado = self.calc.restar(10, 5)
        self.assertEqual(5, resultado)

    def test_restar_cadena(self):
        resultado = self.calc.restar('x', 2)
        self.assertEqual('Solo se aceptan numeros', resultado) 

    def test_restar_num_positivos(self):
        resultado = self.calc.restar(-4, 5)
        self.assertEqual('Solo numeros positivos', resultado)                

    def test_restar_num_enteros(self):
        resultado = self.calc.restar(9.5, 5.2)
        self.assertEqual('Solo numeros enteros', resultado)   

    def test_restar_no_listas(self):
        resultado = self.calc.restar([3,4,5], 2)
        self.assertEqual('Solo acepto numeros no listas', resultado)  

    # Pruebas unitarias para la funcion de dividir 
    def test_dividir_diez_entre_cinco(self):
        resultado = self.calc.dividir(10, 5)
        self.assertEqual(2, resultado)

    def test_dividir_cadena(self):
        resultado = self.calc.dividir('x', 2)
        self.assertEqual('Solo se aceptan numeros', resultado) 

    def test_dividir_num_positivos(self):
        resultado = self.calc.dividir(-4, 5)
        self.assertEqual('Solo numeros positivos', resultado)                

    def test_dividir_num_enteros(self):
        resultado = self.calc.dividir(9.5, 5.2)
        self.assertEqual('Solo numeros enteros', resultado)   

    def test_dividir_no_listas(self):
        resultado = self.calc.dividir([3,4,5], 2)
        self.assertEqual('Solo acepto numeros no listas', resultado)      

    def test_dividir_dos_entre_cero(self):
        resultado = self.calc.dividir(5, 0)
        self.assertEqual('No se puede dividir entre cero', resultado)     

    # Pruebas unitarias para la funcion de multiplicar
    def test_multiplicar_diez_entre_cinco(self): 
        resultado = self.calc.multiplicar(10, 5)
        self.assertEqual(50, resultado)

    def test_multiplicar_cadena_por_dos(self):
        resultado = self.calc.multiplicar('x', 2)
        self.assertEqual('Solo se aceptan numeros', resultado) 

    def test_multiplicar_num_positivos(self):
        resultado = self.calc.multiplicar(-4, 5)
        self.assertEqual('Solo numeros positivos', resultado)                

    def test_multiplicar_num_enteros(self):
        resultado = self.calc.multiplicar(9.5, 5.2)
        self.assertEqual('Solo numeros enteros', resultado)   

    def test_multiplicar_no_listas(self):
        resultado = self.calc.multiplicar([3,4,5], 2)
        self.assertEqual('Solo acepto numeros no listas', resultado)  

    # pruebas unitarias para la funcion de potencia
    def test_potencia_base_entera_exponente_entero(self):
        result = self.calc.potencia(2, 5)
        self.assertEqual(result, 32)

    def test_potencia_base_negativa_exponente_entero(self):
        result = self.calc.potencia(-2, 2)
        self.assertEqual(result, 'Solo numeros positivos para la base')

    def test_potencia_base_no_numerica_exponente_entero(self):
        result = self.calc.potencia("X", 30)
        self.assertEqual(result, 'Solo se aceptan numeros')

    def test_potencia_base_lista_exponente_flotante(self):
        result = self.calc.potencia([4,5,6], 3.5)
        self.assertEqual(result, 'Solo acepto numeros no listas')

    def test_potencia_base_flotante_exponente_entero(self):
        result = self.calc.potencia(3.6, 2)
        self.assertEqual(result, 'Solo numeros enteros para la base, enteros o flotantes para el exponente')    


if __name__ == '__main__': # pragma: no cover
    unittest.main()

