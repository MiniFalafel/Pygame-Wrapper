from enum import Enum

class ForceType(str, Enum):
    CONSTANT        = "CONSTANT"
    CONST_ACCEL     = "CONST_ACCEL"
    IMPULSE         = "IMPULSE"
    ACCELERATE      = "ACCELERATE"

class Force:
    def __init__(self, force_vec: tuple[float, float], f_type: ForceType):
        self.f = force_vec
        self.type = f_type