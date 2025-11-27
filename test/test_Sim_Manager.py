"""
Authors:
Brage Bromset Bestvold
Gabriel Røer
"""


from student_sim.Sim_Manager import SimManager
from student_sim.World import World
from student_sim.Student import Student
from student_sim.Startpoint import Startpoint
from student_sim.Endpoint import Endpoint


def test_init():
    world = World()
    sim = SimManager(world)
    assert sim.world == world


def test_sim_step():
    world = World()
    start = Startpoint("start", 50)
    end = Endpoint("goal", 51, 1)
    student = Student("Alex", start, 1, 1)
    world.add_student(student)
    world.add_startpoint(start)
    world.add_endpoint(end)
    sim = SimManager(world)
    assert sim.world.students[0].time_elapsed == 0
    sim.sim_step()
    assert sim.world.students[0].time_elapsed == 1


def test_sim_run():
    world = World()
    start = Startpoint("start", 50)
    end = Endpoint("goal", 51, 1, 0)
    student = Student("Alex", start, 1, 1)
    world.add_student(student)
    world.add_startpoint(start)
    world.add_endpoint(end)
    sim = SimManager(world, debug=True)
    sim.run()
    assert sim.world.students[0].finished


def test_get_stats():
    world = World()
    start = Startpoint("start", 50)
    end = Endpoint("goal", 51, 1, 0)
    student = Student("Alex", start, 1, 1)
    world.add_student(student)
    world.add_startpoint(start)
    world.add_endpoint(end)
    sim = SimManager(world)
    sim.run()
    stats = sim.get_stats()
    assert stats["avg_steps"] == 1.0
