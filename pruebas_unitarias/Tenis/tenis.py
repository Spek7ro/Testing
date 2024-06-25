class Tenis:
    score_p1 = 0
    score_p2 = 0
    valores = ['0', '15', '30', '40']

    def reset(self):
        self.score_p1 = 0
        self.score_p2 = 0

    def consultar_score(self):
        if self.score_p1 >= 3 and self.score_p2 >= 3:
            if abs(self.score_p1 - self.score_p2) <= 1:
                if self.score_p1 == self.score_p2:
                    self.score_p1 = 'Deuce'
                    self.score_p2 = 'Deuce'
                elif self.score_p1 > self.score_p2:
                    self.score_p1 = 'Ventaja'
                    self.score_p2 = '*'
                else:
                    self.score_p2 = 'Ventaja'
                    self.score_p1 = '*'
                return f"{self.score_p1} - {self.score_p2}"
            if self.score_p1 > self.score_p2:
                return 'win - lost'
            return 'lost - win'
        if self.score_p1 < 4 and self.score_p2 < 4:
            return f"{self.valores[self.score_p1]} - {self.valores[self.score_p2]}"
        if self.score_p1 > self.score_p2:
            return 'win - lost'
        return 'lost - win'

    def score(self, puntos):
        for player in puntos:
            self.score_p1 += 1 if player == 1 else 0
            self.score_p2 += 1 if player == 2 else 0
