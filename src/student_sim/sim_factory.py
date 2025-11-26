from student_sim.World import World
from student_sim.Student import Student
from student_sim.Startpoint import Startpoint
from student_sim.Endpoint import Endpoint
from student_sim.Sim_Manager import SimManager


def create_simulation(
    n_students=1,
    startpoints=[{"name": "AudMax", "position": 50}],
    endpoints=[
        {"name": "Pentagon", "position": 10, "entry_prob": 0.1, "max_capacity": 0},
        {"name": "Kaia", "position": 90, "entry_prob": 0.1, "max_capacity": 0}
    ],
    world_min=0,
    world_max=100,
    move_prob=0.99,
    move_east_prob=0.5
):
    """
    Creates a World object, adds startpoints, endpoints, and students.

    Parameters:
        n_students (int): Number of students to spawn
        startpoints (list of dicts): [{"name": str, "position": int}, ...]
        endpoints (list of dicts): [{"name": str, "position": int, "entry_prob": float, "max_capacity": int}, ...]
        world_min (int): Minimum world coordinate
        world_max (int): Maximum world coordinate
        move_prob (float): Probability that a student moves each second
        move_east_prob (float): Probability that a movement goes east

    Returns:
        world (World): The simulation world
        sim (SimManager): Simulation manager
    """

    #print sim settings norsk
    print("----- Simuleringsinnstillinger")
    print(f"studenter: {n_students}")
    print(f"startpunkter: {startpoints}")
    print(f"endepunkter: {endpoints}")
    print(f"verden minimum: {world_min}")
    print(f"verden maksimum: {world_max}")
    print(f"sannsynlighet for å bevege seg: {move_prob}")
    print(f"sannsynlighet for å bevege seg øst: {move_east_prob}")
    print("------------------------------")

    # Create world with bounds
    world = World(world_min=world_min, world_max=world_max)

    # Add startpoints
    for sp in startpoints:
        world.add_startpoint(Startpoint(sp["name"], position=sp["position"]))

    # Add endpoints
    for ep in endpoints:
        world.add_endpoint(
            Endpoint(
                ep["name"],
                position=ep["position"],
                entry_prob=ep["entry_prob"],
                max_capacity=ep["max_capacity"]
            )
        )

    # Use first startpoint as default spawn location
    default_start = next(iter(world.startpoints.values()))

    # Spawn students
    for i in range(n_students):
        student = Student(
            name=f"Student_{i}",
            startpoint=default_start,
            move_prob=move_prob,
            move_east_prob=move_east_prob,
            world_min=world_min,
            world_max=world_max
        )
        world.add_student(student)

    # Create simulation manager
    sim = SimManager(world)

    return world, sim
