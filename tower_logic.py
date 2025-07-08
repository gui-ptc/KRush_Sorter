import random
from random import choice, shuffle


def tower_sorter(num_slots: int):
    tower_list = ['Arcane', 'Fire', 'Paladin', 'Viking', 'Archer', 'Rifler', 'BB', 'Tesla']
    tower_upgrade_prior = []
    for i in range(1, num_slots + 1):
        torre = choice(tower_list)
        tower_upgrade_prior.append(torre)

    upgrade = tower_upgrade_prior.copy()
    shuffle(upgrade)

    return tower_upgrade_prior, upgrade
