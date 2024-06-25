# test_calificaciones.py
import unittest
from promedio import promedio  

class TestPromedio(unittest.TestCase):

    def test_promedio_normal(self):
        self.assertEqual(promedio(8, 7, 9), 8)

    def test_promedio_negativo(self):
        self.assertEqual(promedio(-2, 6, 5), 'Solo calificaciones mayores a cero')

    def test_promedio_no_numeros(self):
        self.assertEqual(promedio('x', 'y', 9), 'Solo se aceptan numeros')

    def test_promedio_ceros(self):
        self.assertEqual(promedio(0, 0, 0), 'Solo calificaciones mayores a cero')

    def test_promedio_lista_como_entrada(self):
        self.assertEqual(promedio([2,3], 10, 8), 'Solo se aceptan numeros')

    def test_promedio_mayor_que_diez(self):
        self.assertEqual(promedio(12, 7, 18), 'Solo calificaciones menores o iguales a 10')

    def test_promedio_valores_nulos(self):
        self.assertEqual(promedio(None, None, None), 'No se aceptan valores nulos')

if __name__ == '__main__': # pragma: no cover
    unittest.main()
