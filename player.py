import numpy as np

class Player():
    def __init__(self, skill_level, instability = 1):
        self.skill_level = skill_level
        self.instability = instability

    def wins_against(self, other):
        own_performance = np.random.normal(self.skill_level, self.instability)
        other_performance = np.random.normal(other.skill_level, other.instability)
        return own_performance > other_performance

    def get_winner(self, other):
        if self.wins_against(other):
            return self
        else:
            return other
