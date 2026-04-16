class TennisGame1:
    #jedna zmienna od wyników
    SCORE_NAMES = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    # funkcja score tylko od wyniku

    def score(self):
        if self.p1points == self.p2points:
            return f"{self.SCORE_NAMES[self.p1points]}-All" if self.p1points < 3 else "Deuce"
        if self.p1points >= 4 or self.p2points >= 4:
            return self.endgame_score()

        return f"{self.SCORE_NAMES[self.p1points]}-{self.SCORE_NAMES[self.p2points]}"

    ##funkcja od wyniku końca meczu (warto ją ustawić na prywatną)

    def endgame_score(self) -> str:  ## wskazanie na zwracany typ danych
        diff = self.p1points - self.p2points
        if abs(diff) == 1:
            leader = self.player1_name if diff > 0 else self.player2_name
            return f"Advantage {leader}"

        winner = self.player1_name if diff >= 2 else self.player2_name
        return f"Win for {winner}"





