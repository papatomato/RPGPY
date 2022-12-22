from random import randint


class Battle:
    def __init__(self):
        self.enemies = None
        self.battle_queue = None
        self.sorted_queue = None

        # uses random to generate 3 enemies in battle

    def enemy_queue(self, enemies):
        self.enemies = enemies

        for x in range(3):
            self.battle_queue.append(self.enemies[randint(1, len(enemies))])

    def speed_sort(self):
        self.sorted_queue = sorted(self.battle_queue)
