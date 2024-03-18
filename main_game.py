import pygame
from core.application import Application
from entity.player import Player

class MyGame(Application):
    def __init__(self):
        # Parent constructor
        super().__init__((640, 420), "Cool Fuckin' Game", 2)

        # Load an image
        player = Player((0, 0), "assets/textures/smile_face.png")
        self.add_entity(player)

# ENTRY POINT
def main():
    my_game = MyGame()
    my_game.run()

if __name__ == "__main__":
    main()
