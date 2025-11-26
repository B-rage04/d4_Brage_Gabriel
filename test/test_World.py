from student_sim.World import World
from student_sim.Student import Student
from student_sim.Startpoint import Startpoint
from student_sim.Endpoint import Endpoint


def test_world():
    world = World()
    assert world.students == []
    assert world.startpoints == {}
    assert world.endpoints == {}
    assert world.world_min == 0
    assert world.world_max == 100


def test_world2():

    world = World(50, 75)
    assert world.world_min == 50
    assert world.world_max == 75


def test_world_methods():
    world = World()

    start = Startpoint("start", 50)
    end = Endpoint("goal", 20, 0.4)
    student = Student("Alex", start)

    world.add_student(student)
    world.add_startpoint(start)
    world.add_endpoint(end)

    assert world.students == [student]
    assert world.startpoints == {"start": start}
    assert world.endpoints == {"goal": end}
    assert world.get_all_positions() == [student.position]


def test_world_reset():
    world = World()
    start = Startpoint("start", 30)
    student = Student("Alex", start, 1, 1)
    world.add_startpoint(start)
    world.add_student(student)
    student.step()
    assert student.position == 31
    assert student.time_elapsed == 1
    assert student.steps_taken == 1
    world.reset()
    assert student.position == 30
    assert student.time_elapsed == 0
    assert student.time_elapsed == 0
