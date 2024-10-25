from Tile import *
from TileBag import *

# Factory (Disks)
class Factory:
    def __init__(self):
        self.tiles = []

    # Draw tiles from the bag to fill the factory
    def populate_factory(self, bag: TileBag):
        return bag.draw_tiles()

    def __str__(self):
        return f"Factory (tiles={[str(tile) for tile in self.tiles]})"

    # Remove tiles of the specified color from the factory
    def take_tiles(self, color):
        taken_tiles = [tile for tile in self.tiles if tile.color == color]
        self.tiles = [tile for tile in self.tiles if tile.color != color]
        return taken_tiles

