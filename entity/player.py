import pygame

from entity.entity import Entity
from physics.solver import Solver
from physics.force import Force, ForceType
from rendering.spritelib import SpriteLibrary
from core.application import Application

class Player(Entity):
    def __init__(self, pos: list[float, float], sprite_path: str):
        # Parent constructor
        super().__init__("PLAYER", pos)

        # Add a rigidbody component
        self.rigidbody = Solver.create_rigidbody(1.0, self.pos, (0, 0))
        self.add_component(self.rigidbody)

        # Sprite
        self.sprite = SpriteLibrary.load(sprite_path)

        # Keep track of movement input state
        self.move_state = {"Forward": False, "Backward": False, "Left": False, "Right": False}

    # VIRTUAL FUNCTIONS
    # Movement input
    def on_key_input(self, key_code: int, pressed: bool):
        if key_code == pygame.K_w:
            self.move_state["Forward"] = pressed
        if key_code == pygame.K_a:
            self.move_state["Left"] = pressed
        if key_code == pygame.K_s:
            self.move_state["Backward"] = pressed
        if key_code == pygame.K_d:
            self.move_state["Right"] = pressed

    def on_update(self, dt: float):
        move_dir = [0, 0]
        move_dir[0] = self.move_state["Right"] - self.move_state["Left"]
        move_dir[1] = self.move_state["Backward"] - self.move_state["Forward"]


        #print(move_dir)
        # self.pos[0] += move_dir[0] * m
        # self.pos[1] += move_dir[1] * m
        m = 15000 * dt
        move_dir[0] = float(move_dir[0]) * m
        move_dir[1] = float(move_dir[1]) * m
        counter_vel = self.rigidbody.get_velocity()[0] * -7000.0

        move_dir[0] += counter_vel

        self.rigidbody.add_force(Force(move_dir, ForceType.ACCELERATE))

        #print(self.pos)

    def on_render(self):
        # Blit onto the application window
        Application.get_window().blit(self.sprite, self.pos)

