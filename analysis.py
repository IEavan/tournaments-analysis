import numpy as np
from tournaments import Elimination
from player import Player

# Generate Players
def gen_players_seq(num_players, instability):
    players = []
    for i in range(num_players):
        players.append(Player(i, instability = instability))
    return players

times_best_wins = 0
total = 0
players = gen_players_seq(32, 1)
best = players[-1]
elim = Elimination(players)
while True:
    if elim.get_winner() == best:
        times_best_wins += 1
    total += 1
    print("\rProbability that best wins is: {:.4}%".format(times_best_wins * 100 / total), end="")
