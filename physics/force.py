from enum import Enum

class ForceType(str, Enum):
    FORCE       = "FORCE"       # Applies the force, accounting for mass
    ACCELERATE  = "ACCELERATE"  # Does not account for mass, pure acceleration

class Force:
    def __init__(self, force_vec: tuple[float, float], f_type: ForceType):
        self.f_vec = force_vec
        self.type = f_type