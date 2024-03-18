import pygame
from entity.entity_component import ComponentList, EntityComponent
from core.event_handler import EventHandler

class Entity(EventHandler):
    def __init__(self, name: str, pos: list[float, float]):
        self.name = name
        self.pos = list(pos)
        self.components = ComponentList()

    def get_id(self):
        return hash(str(id(self)) + self.name)

    def add_component(self, component: EntityComponent):
        self.components.add(component)

    def remove_component(self, component: EntityComponent):
        self.components.remove(component)

    # Update and render
    def update(self, dt: float):
        # Update components
        self.components.update(dt)
        # Call the callbacks/virtuals
        self.on_update(dt)

    def render(self):
        # Render components
        self.components.render()
        # Call the callbacks/virtuals
        self.on_render()

    def on_update(self, dt: float):
        pass
    def on_render(self):
        pass
