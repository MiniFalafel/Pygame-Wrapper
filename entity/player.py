import pygame

from entity.entity import Entity
from physics.rigidbody import Rigidbody
from rendering.spritelib import SpriteLibrary
from core.application import Application

class Player(Entity):
    def __init__(self, pos: tuple[float, float], sprite_path: str):
        # Parent constructor
        super().__init__("PLAYER", pos)

        # Add a rigidbody component
        self.rigidbody = Rigidbody(1.0, self.pos, (0, 0))
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
        m = 50 * dt
        self.pos[0] += move_dir[0] * m
        self.pos[1] += move_dir[1] * m

        #print(self.pos)

    def on_render(self):
        # Blit onto the application window
        Application.get_window().blit(self.sprite, self.pos)

