from core.application import Application
from rendering.spritelib import SpriteLibrary

class Tile:
    def __init__(self, _type: str, variation: str):
        self.type = _type
        self.variant = variation


class TileMap:
    def __init__(self, tile_size: int):
        self.tilemap = {}
        self.tile_size = tile_size

    def _pos_to_index(self, pos: tuple):
        return str(pos[0]) + ";" + str(pos[1])

    def _index_to_pos(self, index: str):
        sx, sy = index.split(";")
        return [int(sx), int(sy)]

    def render(self):
        # Get Application surface
        surface = Application.get_surface()

        # Get the tiles for lookup
        tile_sprites = SpriteLibrary.get_tiles()
        # Make sure it's been loaded
        assert tile_sprites is not None, "TILE_ERROR: Looks like you haven't loaded in your tile sprites yet!"

        # loop through tile positions
        for pos in self.tilemap:
            tile = self.tilemap[pos]
            # number pos
            numpos = self._index_to_pos(pos)
            surface.blit(tile_sprites[tile["type"]][tile["variant"]], (numpos[0] * self.tile_size, numpos[1] * self.tile_size))

