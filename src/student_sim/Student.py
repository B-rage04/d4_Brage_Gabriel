from .Startpoint import Startpoint
class Student:
    def __init__(self, name: str, startpoint: Startpoint, move_prob: float = 0.2):
        self.name = name
        self.position = startpoint.position
        self.move_prob = move_prob
        self.steps_taken = 0
        self.time_elapsed = 0
        self.finished = False
        self.destination = None

    def step(self):
        """Perform one second of movement."""
        from random import random, choice
        self.time_elapsed += 1
        if random() < self.move_prob:
            direction = choice([-1, 1])  # -1: west, 1: east
            self.position += direction
            self.position = max(0, min(100, self.position))  # keep in bounds
            self.steps_taken += 1
