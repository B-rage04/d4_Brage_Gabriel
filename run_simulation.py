from src.student_sim.World import World
from src.student_sim.Student import Student
from src.student_sim.Startpoint import Startpoint
from src.student_sim.Endpoint import Endpoint
from src.student_sim.Sim_Manager import SimManager
import matplotlib.pyplot as plt

def display_results(world, sim):
    """Prints and plots results of the simulation."""
    print("\n=== Individual Student Results ===")
    print(f"{'Name':<12}{'Destination':<12}{'Steps':<8}{'Time':<8}")
    print("-" * 40)
    for student in world.students:
        dest = student.destination if student.destination else "None"
        print(f"{student.name:<12}{dest:<12}{student.steps_taken:<8}{student.time_elapsed:<8}")

    print("\n=== Summary Statistics ===")
    stats = sim.get_stats()
    print(f"Total students: {stats['total_students']}")
    print(f"Finished students: {stats['finished']}")
    print(f"Average steps taken: {stats['avg_steps']:.2f}")
    print(f"Average time elapsed: {stats['avg_time']:.2f} seconds")
    print("Destination counts:")
    for ep, count in stats['destinations'].items():
        print(f"  {ep}: {count}")

    # --- Graphical display ---
    destinations = [s.destination for s in world.students if s.destination]
    steps = [s.steps_taken for s in world.students]
    times = [s.time_elapsed for s in world.students]

    # 1. Bar chart of destinations
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.bar(stats['destinations'].keys(), stats['destinations'].values(), color='skyblue')
    plt.title("Students per Endpoint")
    plt.ylabel("Number of Students")

    # 2. Histogram of steps
    plt.subplot(1, 3, 2)
    plt.hist(steps, bins=10, color='lightgreen', edgecolor='black')
    plt.title("Distribution of Steps Taken")
    plt.xlabel("Steps")
    plt.ylabel("Number of Students")

    # 3. Histogram of time elapsed
    plt.subplot(1, 3, 3)
    plt.hist(times, bins=10, color='salmon', edgecolor='black')
    plt.title("Distribution of Time Elapsed")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()

def main():
    # Create world
    world = World()

    # Add startpoints and endpoints
    audmax = Startpoint("AudMax", position=50)
    pentagon = Endpoint("Pentagon", position=10, entry_prob=0.1, max_capacity=0)
    kaia = Endpoint("Kaia", position=90, entry_prob=0.8, max_capacity=0)

    world.add_startpoint(audmax)
    world.add_endpoint(pentagon)
    world.add_endpoint(kaia)

    # Spawn multiple students
    n_students = 100
    for i in range(n_students):
        world.add_student(Student(name=f"Student_{i}", startpoint=audmax))

    # Run simulation
    sim = SimManager(world)
    sim.run()

    # Display results
    display_results(world, sim)

if __name__ == "__main__":
    main()
