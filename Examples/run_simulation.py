from student_sim.sim_factory import create_simulation
from student_sim.Graf import plot_simulation
from student_sim.utils import display_results, merge_simulation_data


def main():
    debug = True

    n_sim = 1

    worlds = []
    sims = []

    # Run simulations
    for i in range(n_sim):
        if debug:
            print(f"------------------------- Running simulation {i+1}/{n_sim}")
        world, sim = create_simulation()
        sim.run()  # hadde vert morsomt om de viste sim live
        worlds.append(world)
        sims.append(sim)
        if debug:
            print(f"------------------------- Finished simulation {i+1}/{n_sim}")

    if debug:
        # Display all results
        for i in range(n_sim):
            print(f"------------------------- Results for simulation {i+1}/{n_sim}")
            display_results(worlds[i], sims[i])
            plot_simulation(worlds[i], sims[i])

    world, sim = merge_simulation_data(worlds, sims)

    display_results(world, sim)
    plot_simulation(world, sim)


if __name__ == "__main__":
    main()
