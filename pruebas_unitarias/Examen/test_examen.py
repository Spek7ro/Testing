import unittest
from examen import numeroALetra

class TestNumeroALetra(unittest.TestCase):

    def test_numero_5_unidad(self):
        resultado = numeroALetra(5)
        self.assertEqual(resultado, 'cinco')

    def test_numero_28(self):
        resultado = numeroALetra(28)
        self.assertEqual(resultado, 'veintiocho')

    def test_mil_doscientos_cincuenta(self):
        resultado = numeroALetra(1250)
        self.assertEqual(resultado, 'mil doscientos cincuenta')

    def test_mil_ochocientos_veinticuatro(self):
        resultado = numeroALetra(1824)
        self.assertEqual(resultado, 'mil ochocientos veinticuatro')

    def test_novecientos_mil_trecientos_setenta_y_tres(self):
        resultado = numeroALetra(900373)
        self.assertEqual(resultado, 'novecientos mil trescientos setenta y tres')

    # 8,500,427
    def test_ocho_millones_quinientos_mil_cuatroscientos_veintisiete(self): 
        resultado = numeroALetra(8500427)
        self.assertEqual(resultado, 'ocho millones quinientos mil cuatroscientos veintisiete')  

    # 30,500,427
    def test_treinta_millones_quinientos_mil_cuatroscientos_veintisiete(self): 
        resultado = numeroALetra(30500427)
        self.assertEqual(resultado, 'treinta millones quinientos mil cuatroscientos veintisiete') 

    # 20
    def test_numero_20(self): 
        resultado = numeroALetra(20)
        self.assertEqual(resultado, 'veinte') 

    def test_cadena_de_texto(self):
        resultado = numeroALetra('x')
        self.assertEqual(resultado, 'Solo se aceptan numeros')

    def test_numero_decimal(self):
        resultado = numeroALetra(150.89)
        self.assertEqual(resultado, 'Solo se aceptan numeros enteros')

    def test_numero_negativo(self):
        resultado = numeroALetra(-1200)
        self.assertEqual(resultado, 'Solo se aceptan numeros positivos')

    def test_limite_inferior_superado(self):
        resultado = numeroALetra(1100000000)
        self.assertEqual(resultado, 'Solo se aceptan numeros menores a 1,000,000,000')

    #100,002
    def test_cien_mil_dos(self):
        resultado = numeroALetra(100002)
        self.assertEqual(resultado, 'cien mil dos')

    def test_cien_millones(self):
        resultado = numeroALetra(100000000)
        self.assertEqual(resultado, 'cien millones')  

    def test_ciento_cincuenta_mil_trescientos_sesenta_y_ocho(self):
        resultado = numeroALetra(150368)
        self.assertEqual(resultado, 'ciento cincuenta mil trescientos sesenta y ocho')        

    def test_novecientos_noventa_millones(self):
        resultado = numeroALetra(990000000)
        self.assertEqual(resultado, 'novecientos noventa millones')

if __name__ == '__main__':
    unittest.main()
