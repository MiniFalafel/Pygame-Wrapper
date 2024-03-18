from physics.force import Force, ForceType

from entity.entity_component import EntityComponent

class Rigidbody(EntityComponent):
    def __init__(self, mass: float, pos: list[float, float], init_vel: tuple[float, float]):
        """
        DO NOT USE!!! Instead, create a rigidbody using Solver.create_rigidbody()

        :param mass:
        :param pos:
        :param init_vel:
        """
        self.mass = mass
        self.pos = pos
        self.last_frame_pos = [pos[i] - init_vel[i] for i in range(2)]

        # Initialize forces
        self.forces = []

    def add_force(self, force: Force):
        self.forces.append(force)

    def get_current_acceleration(self):
        # Store total acceleration
        total_accel = [0, 0]
        # Loop through each force
        for force in self.forces:
            m = 1.0 # multiplier for mass effect/non-effect
            # If the force type is FORCE, then m should be 1 / mass
            if force.type == ForceType.FORCE:
                m = 1.0 / self.mass
            # Add the force * multiplier to the total_accel
            total_accel = [total_accel[i] + force.f_vec[i] * m for i in range(2)]

        # Empty the list of forces
        self.forces.clear()
        # return total_accel
        return total_accel

