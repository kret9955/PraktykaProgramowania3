class TennisGame3:
    #rozwinięto nazwy zmiennych aby były bardziej czytelne
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    #wykorzystano atrybuty konstruktora
    def won_point(self, name):
        if name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if (self.p1points < 4 and self.p2points < 4) and (self.p1points + self.p2points < 6):
            point = ["Love", "Fifteen", "Thirty", "Forty"]
            score = point[self.p1points]
            return score + "-All" if (self.p1points == self.p2points) else score + "-" + point[self.p2points]
        else:
            if self.p1points == self.p2points:
                return "Deuce"
            score = self.player1_name if self.p1points > self.p2points else self.player2_name
            return (
                "Advantage " + score
                if ((self.p1points - self.p2points) * (self.p1points - self.p2points) == 1)
                else "Win for " + score
            )
