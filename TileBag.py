from Tile import *
import random

TILE_COUNT = 20 # tiles of each color

class TileBag:
    def __init__(self):
        self.bag = self.populate_bag()
        self.discard = []

    # Start of game
    def populate_bag(self):
        return [Tile(color) for color in TILE_COLORS for _ in range(TILE_COUNT)]  

    # Add tiles to the bag
    def add_to_bag(self, tiles: list[Tile]):
        self.bag.extend(tiles)
    
    # Add tiles to the discard
    def add_to_discard(self, tiles: list[Tile]):
        self.discard.extend(tiles)

    # Used to populate Factory
    def draw_tiles(self, num=4):
        draw = []

        # Try to draw from the bag
        while len(draw) < num and self.bag:
            draw.append(self.bag.pop(random.randint(0, len(self.bag) - 1)))
        
        # If not enough tiles were drawn, check the discard
        if len(draw) < num:
            if self.discard:
                self.add_tiles(self.discard)  # Move discard to the bag
                self.discard.clear()  # Clear the discard pile

                # Continue drawing tiles
                while len(draw) < num and self.bag:
                    draw.append(self.bag.pop(random.randint(0, len(self.bag) - 1)))
        
        return draw       

