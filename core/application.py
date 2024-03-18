import pygame
import sys
from core.window import Window
from core.event_handler import EventHandler
from entity.entity import Entity
from physics.solver import Solver

# APP PREFERENCES
FRAME_RATE = 60

class Application(EventHandler):
    # Static variable keeps track of whether we've initialized yet
    s_instance = None

    def __init__(self, size: tuple = (640, 420), title: str = "My Game", render_upscale: int = 2):
        # CHECK INITIALIZATION
        if self.s_instance is not None:
            raise Exception("APPLICATION_ERROR: Application already initialized!")

        # initialize pygame
        pygame.init()

        # Create our window
        self.window = Window(size, title, render_upscale)
        self.clock = pygame.time.Clock()
        self.last_frame_time = self.clock.get_time()

        # Create a set of entities
        self.entities = {}

        # State tracking
        self.running = False

        # static initialized state
        Application.s_instance = self

    def add_entity(self, entity: Entity):
        self.entities[entity.get_id()] = entity

    def pop_entity(self, entity_id: int):
        return self.entities.pop(entity_id)

    def on_update(self, dt):
        pass
    def on_render(self):
        pass

    def run(self):
        # Set running to true
        self.running = True

        # Game loop
        while self.running:
            # EVENTS
            for event in pygame.event.get():
                # QUIT EVENT
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # EVENT DISPATCHING
                EventHandler.dispatch(self, event) # dispatch to self
                # Dispatch event to entities
                for id, entity in self.entities.items():
                    EventHandler.dispatch(entity, event)

            # Get delta time
            t = pygame.time.get_ticks()
            delta_time = (t - self.last_frame_time) / 1000
            self.last_frame_time = t

            # UPDATES
            # Update entities
            for id, entity in self.entities.items():
                entity.update(delta_time)
            # Update Physics solver
            Solver.update(delta_time)
            # User update
            self.on_update(delta_time)

            # RENDERING
            # Render entities
            for id, entity in self.entities.items():
                entity.render()
            # User draw
            self.on_render()

            # Display window to the screen
            self.window.render()

            # UPDATE DISPLAY
            self.window.update_display()
            # Wait for vsync
            self.clock.tick(FRAME_RATE)

    # UTILITY FUNCTIONS
    @staticmethod
    def get_surface():
        return Application.s_instance.window.display

    @staticmethod
    def get_window():
        return Application.s_instance.window

