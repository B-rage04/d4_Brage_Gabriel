from src.student_sim.sim_factory import create_simulation
from src.student_sim.Graf import plot_simulation
from src.student_sim.utils import display_results

def main():
    n_students = 10
    world, sim = create_simulation(
        n_students=n_students,
        startpoints=[{"name": "AudMax", "position": 50}],
        endpoints=[
            {"name": "Pentagon", "position": 10, "entry_prob": 0.2, "max_capacity":0},
            {"name": "Kaia", "position": 90, "entry_prob": 0.5, "max_capacity": 9}
        ],
        world_min=0,
        world_max=100,
        move_prob=0.80,
        move_east_prob=0.55,
        #max_steps=12*60*60 #12 timer etter event #TODO
    )

    sim.run()

    display_results(world,sim)

    plot_simulation(world, sim)

if __name__ == "__main__":
    main()
