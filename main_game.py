import pygame
from core.application import Application
from rendering.spritelib import SpriteLibrary
from physics.solver import Solver
from entity.player import Player
from rendering.tilemap import TileMap

class MyGame(Application):
    def __init__(self):
        # Parent constructor
        super().__init__((640, 420), "Cool Fuckin' Game", 2)

        # Set gravity to 0
        Solver.set_gravity((0, 0))

        # Load an image
        SpriteLibrary.set_path("assets/textures/")
        SpriteLibrary.load_tiles("tiles")
        player = Player((0, 0), "smile_face.png")
        self.add_entity(player)

        self.tilemap = TileMap(16)

    def on_render(self):
        self.tilemap.render()

# ENTRY POINT
def main():
    my_game = MyGame()
    my_game.run()

if __name__ == "__main__":
    main()
