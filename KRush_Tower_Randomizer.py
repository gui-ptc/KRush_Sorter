import random
from random import choice, shuffle
tower_list = ['Arcane', 'Fire', 'Paladin', 'Viking', 'Archer', 'Rifler', 'BB', 'Tesla']
tower_upgrade_prior = []
for i in range(1,16):
        a = choice(tower_list)
        print(f"{i}º: {a}")
        tower_upgrade_prior.append(a)
shuffle(tower_upgrade_prior)
print(tower_upgrade_prior)
