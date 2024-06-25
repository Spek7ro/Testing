import unittest
from edades import clasificar_edad  

class TestClasificarEdad(unittest.TestCase):

    def test_edad_negativa(self):
        self.assertEqual(clasificar_edad(-1), 'No existes')

    def test_edad_nino(self):
        self.assertEqual(clasificar_edad(0), 'Eres niño')
        self.assertEqual(clasificar_edad(12), 'Eres niño')

    def test_edad_adolescente(self):
        self.assertEqual(clasificar_edad(13), 'Eres adolescente')
        self.assertEqual(clasificar_edad(17), 'Eres adolescente')

    def test_edad_adulto(self):
        self.assertEqual(clasificar_edad(18), 'Eres adulto')
        self.assertEqual(clasificar_edad(64), 'Eres adulto')

    def test_edad_adulto_mayor(self):
        self.assertEqual(clasificar_edad(65), 'Eres adulto mayor')
        self.assertEqual(clasificar_edad(119), 'Eres adulto mayor')

    def test_edad_mumm_ra(self):
        self.assertEqual(clasificar_edad(120), 'Eres Mumm-Ra')
        self.assertEqual(clasificar_edad(150), 'Eres Mumm-Ra')

    def test_edad_no_entero(self):
        self.assertEqual(clasificar_edad("X"), 'Solo se aceptan números enteros')
        self.assertEqual(clasificar_edad(25.5), 'Solo se aceptan números enteros')
        self.assertEqual(clasificar_edad(None), 'Solo se aceptan números enteros')
        self.assertEqual(clasificar_edad([3, 6, 5]), 'Solo se aceptan números enteros')

if __name__ == '__main__': # pragma: no cover
    unittest.main()
