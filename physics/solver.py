from physics.rigidbody import Rigidbody
from physics.force import Force, ForceType

class Solver:
    # Static list of all rigid bodies
    _s_Rigidbodies = []
    _s_Gravity = Force((0, 300), ForceType.ACCELERATE)
    _s_SimResolution = 4 # Number of steps per frame in simulation - TODO: Make fixed rate on separate thread

    @staticmethod
    def set_resolution(num_steps: int):
        Solver._s_SimResolution = num_steps

    # Static methods for creating rigidbodies
    @staticmethod
    def create_rigidbody(mass: float, pos: list[float, float], init_vel: tuple[float, float]):
        r = Rigidbody(mass, pos, init_vel)
        Solver._s_Rigidbodies.append(r)
        return r

    @staticmethod
    def remove_rigidbody(r: Rigidbody):
        try:
            Solver._s_Rigidbodies.remove(r)
        except ValueError:
            assert False, "Could not remove Rigidbody because it does not exist!"

    @staticmethod
    def set_gravity(force_vector: tuple[float, float]):
        Solver._s_Gravity = Force(force_vector, ForceType.ACCELERATE)

    # Updating methods
    @staticmethod
    def apply_gravity():
        for body in Solver._s_Rigidbodies:
            body.add_force(Solver._s_Gravity)

    @staticmethod
    def update_positions(dt: float):
        for body in Solver._s_Rigidbodies:
            # calculate velocity from current pos and last frame's pos
            vel = [body.pos[i] - body.last_frame_pos[i] for i in range(2)]

            # Update self.last_frame_pos
            body.last_frame_pos = list(body.pos)

            # Get acceleration on body
            acc = body.get_current_acceleration()

            # Verlet integrate: pos += vel * acc * dt^2
            body.pos[1] += vel[1] + acc[1] * dt * dt
            body.pos[0] += vel[0] + acc[0] * dt * dt

            # dumb temportary constraint
            if body.pos[1] > 210:
                body.pos[1] = 0
                body.last_frame_pos[1] = 0

    @staticmethod
    def update(dt: float):
        for i in range(Solver._s_SimResolution):
            delta_time = dt / Solver._s_SimResolution
            # Apply gravity and then update positions
            Solver.apply_gravity()
            Solver.update_positions(delta_time)

