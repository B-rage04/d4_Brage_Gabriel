from src.student_sim.sim_factory import create_simulation
from src.student_sim.Graf import plot_simulation
from src.student_sim.utils import display_results

def main():

    n_sim = 40

    worlds = []
    sims = []

    # Run simulations
    for _ in range(n_sim):
        world, sim = create_simulation()
        sim.run()
        worlds.append(world)
        sims.append(sim)

    # Display all results
    for i in range(n_sim):
        display_results(worlds[i], sims[i])
        plot_simulation(worlds[i], sims[i])
        #TODO sammenføy data til plots


if __name__ == "__main__":
    main()
