from student_sim.sim_factory import create_simulation
from student_sim.Graf import plot_simulation
from student_sim.utils import display_results


def main():

    n_sim = 30

    worlds = []
    sims = []

    # Run simulations
    for _ in range(n_sim):
        print(f"------------------------- Running simulation {_+1}/{n_sim}")
        world, sim = create_simulation()
        sim.run() #hadde vert morsomt om de viste sim live
        worlds.append(world)
        sims.append(sim)
        print(f"------------------------- Finished simulation {_+1}/{n_sim}")

    # Display all results
    for i in range(n_sim):
        print(f"------------------------- Results for simulation {i+1}/{n_sim}")
        display_results(worlds[i], sims[i])
        plot_simulation(worlds[i], sims[i])
        # TODO sammenføy data til en plot(s).

    display_results(world, sim)
    plot_simulation(world, sim)

if __name__ == "__main__":
    main()
