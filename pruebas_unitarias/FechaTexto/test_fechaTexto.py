import unittest
from fechaTexto import fechaTexto


class TestFechaTexto(unittest.TestCase):

    def test_fecha_valida_dia_mes_un_digito(self):
        res_obtenido = fechaTexto("5/3/2023")
        res_esperado = "Día cinco de Marzo de dos mil veintitres."
        self.assertEqual(res_obtenido, res_esperado)

    def test_fecha_valida(self):
        res_obtenido = fechaTexto("21/11/1980")
        res_esperado = "Día veintiuno de Noviembre de mil novecientos ochenta."
        self.assertEqual(res_obtenido, res_esperado)

    def test_dia_invalido(self):
        res_obtenido = fechaTexto("32/01/2000")
        res_esperado = "Día inválido"
        self.assertEqual(res_obtenido, res_esperado)

    def test_mes_con_dia_limite(self):
        res_obtenido = fechaTexto("31/3/2024")
        res_esperado = "Día treinta y uno de Marzo de dos mil veinticuatro."
        self.assertEqual(res_obtenido, res_esperado)

    def test_fecha_con_mes_negativo(self):
        res_obtenido = fechaTexto("19/-09/2024")
        res_esperado = "Mes inválido"
        self.assertEqual(res_obtenido, res_esperado)

    def test_fecha_con_año_negativo(self):
        res_obtenido = fechaTexto("12/12/-100")
        res_esperado = "Año inválido"
        self.assertEqual(res_obtenido, res_esperado)

    def test_mes_invalido_fuera_del_rango(self):
        res_obtenido = fechaTexto("12/13/1990")
        res_esperado = "Mes inválido"
        self.assertEqual(res_obtenido, res_esperado)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
