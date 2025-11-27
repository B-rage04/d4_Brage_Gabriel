"""
Authors:
Brage Bromset Bestvold
Gabriel Røer
"""


import pytest
from student_sim.Startpoint import Startpoint


@pytest.mark.parametrize(
                        "name, position",
                        [("Brage", 45),
                         ("Gabriel", 13),
                         ("Alex", 76)])
def test_Startpoint(name, position):
    startpoint = Startpoint(name, position)
    assert startpoint.name == name and startpoint.position == position
