import unittest
from ejercicio import Ejercicio

class TestEjercici(unittest.TestCase):

    def setUp(self):
        self.eje = Ejercicio()

    def test_calcular_monto_total_precio_cantidad(self):
        resultado = self.eje.calcular_monto_total(5,10)
        self.assertEqual(50, resultado)

    def test_calcular_monto_total_precio_cantidad_negativa(self):
        resultado = self.eje.calcular_monto_total(-5,-3)
        self.assertEqual('El precio y la cantidad deben ser numeros positivos', resultado)

    def test_calcular_monto_total_cantidad_entera(self):
        resultado = self.eje.calcular_monto_total(5,4.6)
        self.assertEqual('La cantidad debe ser un numero entero', resultado)

    def test_calcular_monto_total_precio_decimal_entero(self):
        resultado = self.eje.calcular_monto_total('d',6)
        self.assertEqual('El precio debe ser un numero entero o decimal', resultado)


if __name__ == '__main__': # pragma: no cover
    unittest.main()
