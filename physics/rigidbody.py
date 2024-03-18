from physics.force import Force, ForceType

from entity.entity_component import EntityComponent

class Rigidbody(EntityComponent):
    def __init__(self, mass: float, pos: tuple[float, float], init_vel: tuple[float, float]):
        self.mass = mass
        self.pos = pos
        self.last_frame_pos = [pos[i] - init_vel[i] for i in range(2)]

        # Initialize forces
        self.forces = {
            ForceType.CONSTANT:     [], # 'constant' never go away
            ForceType.CONST_ACCEL:  [], # 'const accel' never go away and do NOT account for mass (like gravity)
            ForceType.IMPULSE:      [], # 'impulse' last one frame
            ForceType.ACCELERATE:   [], # 'accelerate' don't account for mass, only directly add to velocity
        }

    def add_force(self, force: Force):
        self.forces[force.type].append(force)

    def get_total_active_force(self):
        # Store total
        total_force = [0, 0]
        updated_forces = dict(self.forces)
        # Loop through all forces and their types
        for t, forces in self.forces.items():
            # Loop through each force
            for force in forces:
                m = 1.0 # multiplier for mass effect/non-effect
                # Also remove the forces from their lists if they aren't constant
                match t:
                    case ForceType.CONSTANT:
                        # Affected by mass, DON'T remove
                        m /= self.mass
                    case ForceType.IMPULSE:
                        # Affected by mass, DO remove
                        m /= self.mass
                        updated_forces[t].remove(force)
                    case ForceType.ACCELERATE:
                        # Not affected by mass, DO remove
                        updated_forces[t].remove(force)
                # Add the force * multiplier to the total_force
                total_force = [total_force[i] + force.f[i] * m for i in range(2)]

        # Update self.forces to match the updated_forces dictionary
        self.forces = updated_forces
        # return total_force
        return total_force

    # OVERRIDE
    def update(self, dt: float):
        # calculate velocity from current pos and last frame's pos
        vel = [self.pos[i] - self.last_frame_pos[i] for i in range(2)]

        # Get all active forces
        acc = self.get_total_active_force()

        # Verlet integrate: pos += vel * acc * dt^2
        self.pos = [self.pos[i] + vel[i] + acc[i] * dt * dt for i in range(2)]

