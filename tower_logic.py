import random
from random import choice, shuffle


def tower_sorter(num_slots: int):
    from collections import Counter
    towers = ['Arcane', 'Fire', 'Paladin', 'Viking', 'Archer', 'Rifler', 'BB', 'Tesla']

    raw = [choice(towers) for _ in range(num_slots)]

    counts = Counter()
    tower_list = []
    for t in raw:
        counts[t] += 1
        tower_list.append(f'{t}{counts[t]}')


    slots = list(range(1, num_slots + 1))
    shuffle(slots)

    slots = list(range(1, num_slots + 1))
    shuffle(slots)
    tower_placement = list(zip(slots, tower_list))

    upgrade = tower_list.copy()
    shuffle(upgrade)

    return tower_placement, upgrade

