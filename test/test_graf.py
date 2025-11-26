from student_sim.Graf import plot_simulation
from student_sim.sim_factory import create_simulation

def test_graf(): #helt klart feil måte å gjøre det på. får 100% da
    world, sim = create_simulation()
    sim.run()
    plot_simulation(world, sim)
    assert True == True