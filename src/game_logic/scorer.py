class Score:
    def __init__(self, start_score=100):
        self.score = start_score


    def decrement_score(self, penalty=5):
        """Decrease the score by a certain penalty."""
        self.score -= penalty
        self.score = max(self.score, 0)

        return self.score


    def return_score(self):
        """Return the current score."""
        return self.score
