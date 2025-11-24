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
