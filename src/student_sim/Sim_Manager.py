
from student_sim.World import World


class SimManager:
    def __init__(self, world: World, debug=False):
        self.world = world
        self.debug = debug

    def sim_step(self):
        """Advance all students by one second."""
        for student in self.world.students:
            if student.finished:
                continue
            student.step()
            # Check if student can enter any endpoint
            for ep in self.world.endpoints.values():
                if student.position == ep.position and ep.try_enter():
                    student.finished = True
                    student.destination = ep.name
                    break

    def run(self):
        """Run simulation until all students finish."""
        i = 0
        
        while not all(s.finished for s in self.world.students):
            if self.debug == True:
                if i < 1000:
                    if i % 100 == 0:
                        print(f"SimTime: {i} seconds")
                if 1000 <= i < 10000:
                    if i % 500 == 0:
                        print(f"SimTime: {i} seconds")
                if i >= 10000:
                    if i % 1000 == 0:
                        print(f"SimTime: {i} seconds")

            self.sim_step()
            i += 1

    def get_stats(self):
        """Return summary stats."""
        stats = {
            'total_students': len(self.world.students),
            'finished': sum(s.finished for s in self.world.students),
            'destinations': {},
            'avg_steps': sum(s.steps_taken for s in self.world.students)/len(self.world.students),
            'avg_time': sum(s.time_elapsed for s in self.world.students)/len(self.world.students)
        }
        for ep_name in self.world.endpoints:
            stats['destinations'][ep_name] = sum(
                s.destination == ep_name for s in self.world.students
            )
        return stats
