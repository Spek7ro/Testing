import unittest
from tenis import Tenis

class TestTenis(unittest.TestCase):

    def setUp(self):
        self.juego = Tenis()

    def test_score_0_0(self):
        self.juego.reset()
        score = self.juego.consultar_score()
        self.assertEqual('0 - 0', score)

    def test_score_40_0(self):
        self.juego.reset()
        self.juego.score([1, 1, 1])
        score = self.juego.consultar_score()
        self.assertEqual('40 - 0', score)

    def test_score_15_30(self):
        self.juego.reset()
        self.juego.score([2, 2, 1])
        score = self.juego.consultar_score()
        self.assertEqual('15 - 30', score)

    def test_score_deuce_deuce(self):
        self.juego.reset()
        self.juego.score([1, 2, 2, 2, 1, 1])
        score = self.juego.consultar_score()
        self.assertEqual('Deuce - Deuce', score)

    def test_score_adv_0(self):
        self.juego.reset()
        self.juego.score([1, 2, 2, 2, 1, 1, 1])
        score = self.juego.consultar_score()
        self.assertEqual('Ventaja - *', score)

    def test_score_0_adv(self):
        self.juego.reset()
        self.juego.score([1, 2, 2, 2, 1, 1, 2])
        score = self.juego.consultar_score()
        self.assertEqual('* - Ventaja', score)

    def test_score_lost_win(self):
        self.juego.reset()
        self.juego.score([2, 2, 1, 2, 2])
        score = self.juego.consultar_score()
        self.assertEqual('lost - win', score)

    def test_score_win_lost(self):
        self.juego.reset()
        self.juego.score([1, 1, 1, 1])
        score = self.juego.consultar_score()
        self.assertEqual('win - lost', score)

    def test_score_lost2_win2(self):
        self.juego.reset()
        self.juego.score([1, 1, 1, 2, 2, 2, 2, 2])
        score = self.juego.consultar_score()
        self.assertEqual('lost - win', score)
    
    def test_score_win2_lost2(self):
        self.juego.reset()
        self.juego.score([2, 2, 2, 1, 1, 1, 1, 1])
        score = self.juego.consultar_score()
        self.assertEqual('win - lost', score)

if __name__ == '__main__': # pragma: no cover
    unittest.main()
