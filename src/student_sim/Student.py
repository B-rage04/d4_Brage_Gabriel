from .Startpoint import Startpoint
from random import random

class Student:
    def __init__(self, name: str, startpoint: Startpoint, move_prob: float = 0.2, move_east_prob: float = 0.5, world_min: int = 0, world_max: int = 100):
        self.name = name
        self.position = startpoint.position
        self.move_prob = move_prob           # probability of taking a step each second
        self.move_east_prob = move_east_prob # probability step is east
        self.world_min = world_min
        self.world_max = world_max
        self.steps_taken = 0
        self.time_elapsed = 0
        self.finished = False
        self.destination = None
        self.history = []  # (position, move_direction)

    def step(self):
        """Perform one second of movement and record history."""
        self.time_elapsed += 1
        move_dir = 'none'

        if random() < self.move_prob:
            # Determine direction using move_east_prob
            if random() < self.move_east_prob:
                direction = 1
                move_dir = 'east'
            else:
                direction = -1
                move_dir = 'west'

            self.position += direction
            # Keep within world bounds
            self.position = max(self.world_min, min(self.world_max, self.position))
            self.steps_taken += 1

        self.history.append((self.position, move_dir))
