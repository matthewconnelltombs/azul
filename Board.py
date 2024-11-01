from Tile import *

TILE_COLORS = ['BLUE', 'ORANGE', 'RED', 'BLACK', 'WHITE']
TILE_COLORS = [Tile(col) for col in TILE_COLORS]

# Player Board
class Board:
    def __init__(self, col_list: list):
        self.lines = [[None for _ in range(row+1)] for row in range(5)]        
        self.board = [[None for _ in range(5)] for _ in range(5)]
        self.floor = []
        self.score = 0

        self.col_board = [[col_list[(col-row)%5] for col in range(5)] for row in range(5)]
        self.floor_score = [-1, -1, -2, -2, -2, -3, -3]

    # prints a board
    def display_board(self):
        print("Player Lines:")
        for row in self.lines:
            print([str(t) if t is not None else 'None' for t in row])
        
        print("Player Board:")
        for row in self.board:
            print([str(t) if t is not None else 'None' for t in row])
        
        print("Player Floor:")
        print([str(t) if t is not None else 'None' for t in self.floor])

    # checks if a board can add a set of tiles to a row
    def can_add(self, row: int, tiles: list[Tile]):
        # Check if the color is already in the board
        if tiles[0] in self.board[row]:
            return False

        # Check if the line is empty
        if all(color is None for color in self.lines[row]):
            return True

        # Check if the line has that color & has space
        if tiles[0] in self.lines[row] and None in self.lines[row]:
            return True

        return False    

    # adds a set of tiles to a row
    def add_tiles(self, row: int, tiles: list[Tile]):
        # Loop over ever tile spot in the line checking if its empty    
        for i in range(len(self.lines[row])):
            if self.lines[row][i] is None:
                if tiles:
                    self.lines[row][i] = tiles.pop(0)
                else:
                    break
        
        self.floor.extend(tiles)

    # helper function for score_board
    def calc_length(self, row_i, col_i, dir, is_ver):
        length = 0
        iter = 1

        # we use is_ver to zero out the direction we are not checking
        while True:
            # checks if we are off the board
            if col_i + dir*iter*(1-is_ver) > 4 or col_i + dir*iter*(1-is_ver) < 0 or \
               row_i + dir*iter*is_ver     > 4 or row_i + dir*iter*is_ver     < 0:
                break

            # checks if the tile is blank/stop scoring
            if self.board[row_i + is_ver*dir*iter][col_i + (1-is_ver)*dir*iter] is None:
                break

            length += 1
            iter += 1
        
        return length

    # end of round scoring function
    def score_board(self):
        for row_i in range(len(self.lines)):
            if all(tile is not None for tile in self.lines[row_i]):
                col_i = self.col_board[row_i].index(self.lines[row_i][0])

                h, v = 1, 1

                for dir in [-1,1]:
                    v += self.calc_length(row_i, col_i, dir, is_ver=True) # Vertical
                    h += self.calc_length(row_i, col_i, dir, is_ver=False) # Horizontal

                self.score += 1 if (v == 1 and h == 1) else (v + h if (v > 1 and h > 1) else max(v, h))

                self.board[row_i][col_i] = self.lines[row_i][0]
                self.lines[row_i] = [None for _ in self.lines[row_i]]

        floor_pts = sum(self.floor_score[:min(len(self.floor), len(self.floor_score))])
        self.floor.clear()
        self.score += floor_pts
    
    # check if game ends
    def game_end(self):
        for row in self.board:
            if all(tile is not None for tile in row):
                return True
        return False

    # end of game scoring
    def end_score(self):
        complete_rows = 0

        for row in self.board:
            if all(tile is not None for tile in row):
                complete_rows += 1
        
        complete_cols = 0

        for col_i in range(len(self.board[0])):
            if all(self.board[row_i][col_i] is not None for row_i in range(len(self.board))):
                complete_cols += 1

        tile_count = {}

        for row in self.board:
            for t in row:
                if not None:
                    tile_count[t] = tile_count.get(t, 0) + 1

        complete_sets = sum(1 for value in tile_count.values() if value == 5)

        self.score += complete_rows * 2 + complete_cols * 7 + complete_sets * 10

