"""
Authors:
Brage Bromset Bestvold
Gabriel Røer
"""


from copy import deepcopy
from student_sim.Sim_Manager import SimManager


def display_results(world, sim):
    """Prints and plots results of the simulation."""
    print("\n=== Individual Student Results ===")
    print(f"{'Name':<12}{'Destination':<12}{'Steps':<8}{'Time':<8}")
    print("-" * 40)
    for student in world.students:
        dest = student.destination if student.destination else "None"
        print(f"{student.name:<20}{dest:<15}{student.steps_taken:<8}{student.time_elapsed:<8}")

    print("\n=== Summary Statistics ===")
    stats = sim.get_stats()
    print(f"Total students: {stats['total_students']}")
    print(f"Finished students: {stats['finished']}")
    print(f"Average steps taken: {stats['avg_steps']:.2f}")
    print(f"Average time elapsed: {stats['avg_time']:.2f} seconds")
    print("Destination counts:")
    for ep, count in stats['destinations'].items():
        print(f"  {ep}: {count}")


def merge_simulation_data(worlds, sims):
    """Merges data from multiple simulations for combined analysis.

    Returns a new World containing all students (deep-copied) and a new
    SimManager bound to that merged world so stats are computed consistently.
    """
    if not worlds:
        return None, None

    # Start with a deep copy of the first world, but clear its students
    merged_world = deepcopy(worlds[0])
    merged_world.students = []

    # Reset endpoint occupancies in the merged world
    for ep in merged_world.endpoints.values():
        ep.current_occupancy = 0

    # Merge students from all worlds (deep copies to avoid shared state)
    for run_idx, w in enumerate(worlds):
        for s in w.students:
            s_copy = deepcopy(s)
            # ensure unique student names so aggregated reports are clear
            s_copy.name = f"{s_copy.name}_run{run_idx}"
            merged_world.students.append(s_copy)

    # Create a SimManager for the merged world; get_stats will compute aggregates
    merged_sim = SimManager(merged_world)
    return merged_world, merged_sim
