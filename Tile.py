# Game Tiles
class Tile:
    def __init__(self, color):
        self.color = color

    # Check for equality based on color
    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.color == other.color
        return False

    def __str__(self):
        return f"Tile (color={self.color})"

