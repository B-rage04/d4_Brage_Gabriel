from .Student import Student
from .Startpoint import Startpoint
from .Endpoint import Endpoint
from .Endpoint import Endpoint

class World:
    def __init__(self):
        self.students = []
        self.startpoints = {}
        self.endpoints = {}

    def add_student(self, student: Student):
        self.students.append(student)

    def add_startpoint(self, sp: Startpoint):
        self.startpoints[sp.name] = sp

    def add_endpoint(self, ep: Endpoint):
        self.endpoints[ep.name] = ep
