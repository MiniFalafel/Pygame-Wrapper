import pygame

class WindowData:
    def __init__(self, size: tuple, title: str, upscaling: int):
        self.size = size
        self.title = title
        self.upscaling = upscaling

class Window:
    def __init__(self, win_dim: tuple, title: str, upscaling: int):
        # Store data in window data object (easier for if we need to pass this information elsewhere later
        self.win_data = WindowData(win_dim, title, upscaling)
        # Create the pygame screen surface
        pygame.display.set_caption(self.win_data.title)
        self.screen = pygame.display.set_mode(win_dim)

        # Create our rendering surface (account for upscaling)
        self.display = pygame.Surface((self.win_data.size[0] // self.win_data.upscaling, self.win_data.size[1] // self.win_data.upscaling))

    def clear(self, color: tuple[int, int, int]):
        self.display.fill(color)

    def update_display(self):
        # Update pygame display
        pygame.display.update()

    def blit(self, surface: pygame.Surface, pos: tuple):
        self.display.blit(surface, pos)

    def render(self):
        self.screen.blit(pygame.transform.scale(self.display, self.win_data.size), (0, 0))


