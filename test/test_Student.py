"""
Authors:
Brage Bromset Bestvold
Gabriel Røer
"""


import pytest
from student_sim.Student import Student
from student_sim.Startpoint import Startpoint
from random import seed
seed = seed(123)


@pytest.mark.parametrize("name, startpoint, move_prob, move_east_prob, world_min, world_max",
                         [("Alex", Startpoint("AudMax", 50), 0.2, 0.5, 0, 100),
                          ("Brage", Startpoint("AudMax", 25), 0.7, 0.8, 12, 38)])
def test_student(name, startpoint, move_prob, move_east_prob, world_min, world_max):
    stud = Student(name, startpoint, move_prob, move_east_prob, world_min, world_max)

    assert stud.name == name
    assert stud.position == startpoint.position
    assert stud.move_prob == move_prob
    assert stud.move_east_prob == move_east_prob
    assert stud.world_min == world_min
    assert stud.world_max == world_max
    assert stud.steps_taken == 0
    assert stud.time_elapsed == 0
    assert not stud.finished
    assert stud.destination is None
    assert stud.history == []


def test_student_step():
    Alex = Student("Alex", Startpoint("AudMax", 50), 1, 0.5, 0, 100)
    Alex.step()
    assert Alex.position == 49 or Alex.position == 51
    assert Alex.time_elapsed == 1
    assert Alex.steps_taken == 1
