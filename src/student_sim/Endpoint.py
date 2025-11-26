class Endpoint:
    def __init__(self, name: str, position: int, entry_prob: float, max_capacity: int = None):
        self.name = name
        self.position = position
        self.entry_prob = entry_prob
        self.max_capacity = max_capacity
        self.current_occupancy = 0

    def try_enter(self) -> bool:
        """Student tries to enter endpoint."""
        if self.max_capacity == 0:
            self.current_occupancy += 1
            return True

        if self.max_capacity is not None and self.current_occupancy >= self.max_capacity:
            return False
        from random import random
        if random() < self.entry_prob:
            self.current_occupancy += 1
            return True
        return False
