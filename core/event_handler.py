import pygame

class EventHandler:

    @staticmethod
    def dispatch(event_handler, event: pygame.event):
        match event.type:
            # Key press/release
            case pygame.KEYDOWN:
                event_handler.on_key_input(event.key, True)
            case pygame.KEYUP:
                event_handler.on_key_input(event.key, False)
            # Mouse button press/release
            case pygame.MOUSEBUTTONDOWN:
                event_handler.on_mouse_button_input(event.button, True)
            case pygame.MOUSEBUTTONUP:
                event_handler.on_mouse_button_input(event.button, False)
            # Mouse and scroll offsets
            case pygame.MOUSEMOTION:
                event_handler.on_mouse_move(pygame.mouse.get_pos(), pygame.mouse.get_rel())
            case pygame.MOUSEWHEEL:
                event_handler.on_mouse_wheel((event.x, event.y))

    # OVERRIDABLES (for event dispatch)
    def on_key_input(self, key_code: int, pressed: bool):
        pass
    def on_key_repeat(self, key_code: int):
        pass
    def on_mouse_button_input(self, mouse_code: int, pressed: bool):
        pass
    def on_mouse_move(self, pos: tuple, offset: tuple):
        pass
    def on_mouse_wheel(self, offset: tuple):
        pass