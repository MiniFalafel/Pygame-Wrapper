import pygame

class EntityComponent:
    # All entity components will be able to override these functions
    def start(self):
        pass
    def stop(self):
        pass
    def update(self, dt):
        pass
    def render(self):
        pass


class ComponentList:
    def __init__(self):
        self.components = list() # array of EntityComponent objects

    def add(self, component: EntityComponent):
        # Start the component
        component.start()
        # Add to the list
        self.components.append(component)

    def remove(self, component: EntityComponent):
        # Stop the component
        component.stop()
        # Remove from the list
        self.components.remove(component)

    def update(self, dt: float):
        # Update all components
        for ec in self.components:
            ec.update(dt)

    def render(self):
        # Render all components
        for ec in self.components:
            ec.render()