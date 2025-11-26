import pytest
from student_sim.Endpoint import Endpoint
from random import seed
seed = seed(123)


@pytest.mark.parametrize(
        "name, position, entry_prob, max_capasity",
        [("Kaia", 50, 0.5, 5),
         ("Pentagon", 30, 0.2, 0)])
def test_endpoint(name, position, entry_prob, max_capasity):
    end = Endpoint(name, position, entry_prob, max_capasity)
    assert end.name == name
    assert end.position == position
    assert end.entry_prob == entry_prob
    assert end.max_capacity == max_capasity
    assert end.current_occupancy == 0


def test_try_enter1():
    end = Endpoint("Pentagon", 30, 0.5, 0)
    assert end.try_enter()


def test_try_enter2():
    end = Endpoint("Kaia", 50, 0.5, 3)
    assert end.try_enter()


def test_try_enter3():
    end = Endpoint("AudMax", 15, 0.05, 2)
    assert not end.try_enter()


def test_try_enter4():
    end = Endpoint("Rema1000", 74, .76, 1)
    end.current_occupancy = 4
    assert not end.try_enter()
