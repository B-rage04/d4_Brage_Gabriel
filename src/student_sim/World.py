"""
Authors:
Brage Bromset Bestvold
Gabriel Røer
"""


from .Student import Student
from .Startpoint import Startpoint
from .Endpoint import Endpoint


class World:
    def __init__(self, world_min: int = 0, world_max: int = 100):
        self.students = []
        self.startpoints = {}
        self.endpoints = {}
        self.world_min = world_min
        self.world_max = world_max

    def add_student(self, student: Student):
        """Add a student to the world."""
        self.students.append(student)

    def add_startpoint(self, sp: Startpoint):
        """Add a startpoint to the world."""
        self.startpoints[sp.name] = sp

    def add_endpoint(self, ep: Endpoint):
        """Add an endpoint to the world."""
        self.endpoints[ep.name] = ep

    def get_all_positions(self):
        """Return a list of current positions of all students."""
        return [s.position for s in self.students]

    def reset(self):
        """Reset all students to their startpoints and clear histories."""
        for s in self.students:
            s.position = list(self.startpoints.values())[0].position
            s.steps_taken = 0
            s.time_elapsed = 0
            s.finished = False
            s.destination = None
            s.history.clear()
