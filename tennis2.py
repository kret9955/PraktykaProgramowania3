class TennisGame2:
    #wprowadzenie score names
    SCORE_NAMES = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty", }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    #tu przeniesiono to co robią cztery usunięte funkcje
    #używany jest atrybut player_name
    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    #rozbito przypadki na kilka funkcji

    def equal_score(self):
        if self.p1points < 3:
            return f"{self.SCORE_NAMES[self.p1points]}-All"
        return "Deuce"

    def endgame_score(self):
        diff = self.p1points - self.p2points
        distance = abs(diff)
        leader = self.player1_name if diff > 0 else self.player2_name

        if distance == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"

    def score(self):
        if self.p1points == self.p2points:
            return self.equal_score()

        if self.p1points >= 4 or self.p2points >= 4:
            return self.endgame_score()

        return f"{self.SCORE_NAMES[self.p1points]}-{self.SCORE_NAMES[self.p2points]}"




