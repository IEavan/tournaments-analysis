import numpy as np
from player import Player

class Elimination():
    def __init__(self, players):
        if np.log2(len(players)) != int(np.log2(len(players))):
            raise ValueError("Number of players must be a power of 2")
        self.players = players

    def get_brackets(self):
        brackets = []
        brackets.append(self.players)
        while len(brackets[-1]) > 1:
            next_bracket = []
            for i in range(0, len(brackets[-1]), 2):
                next_bracket.append(brackets[-1][i].get_winner(brackets[-1][i+1]))
            np.random.shuffle(next_bracket)
            brackets.append(next_bracket)
        return brackets

    def get_winner(self):
        brackets = self.get_brackets()
        return brackets[-1][0]
