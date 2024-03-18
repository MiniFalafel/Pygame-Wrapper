import pygame

# Class stores all loaded sprites in a static dictionary for lookup
class SpriteLibrary:
    s_sprite_data = {}
    s_base_path = ""
    s_color_key = (0, 0, 0)

    @staticmethod
    def set_path(path: str):
        SpriteLibrary.s_base_path = path

    @staticmethod
    def set_color_key(color: tuple[int, int, int]):
        SpriteLibrary.s_color_key = color

    @staticmethod
    def load(path: str): # This is the type of thing that in C++ I would return a const reference of instead of letting users directly change what's being stored.
        # Generate a key for the sprite
        _k = hash(path)
        # Check if it is already in the loaded data
        if _k in SpriteLibrary.s_sprite_data:
            # Return already loaded data
            return SpriteLibrary.s_sprite_data[_k]

        # Otherwise, load the data and store at that key
        sprite_img = pygame.image.load(SpriteLibrary.s_base_path + path).convert()
        sprite_img.set_colorkey(SpriteLibrary.s_color_key)

        SpriteLibrary.s_sprite_data[_k] = sprite_img
        # RETURN
        return sprite_img
