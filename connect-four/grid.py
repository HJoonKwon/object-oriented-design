import enum


class PieceColor(enum.Enum):
    Empty = 0
    Red = 1
    Blue = 2


class Grid:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self.init_grid()

    def init_grid(self):
        self._grid = [
            [PieceColor.Empty for _ in range(self._cols)] for _ in range(self._rows)
        ]

    def get_rows(self):
        return self._rows

    def get_cols(self):
        return self._cols

    def get_piece(self, row: int, col: int) -> PieceColor:
        assert row >= 0 and row < self._rows
        assert col >= 0 and col < self._cols
        return self._grid[row][col]

    def set_piece(self, col: int, color: PieceColor) -> bool:
        assert color in [PieceColor.Empty, PieceColor.Red, PieceColor.Blue]
        assert col >= 0 and col < self._cols
        for row in range(self._rows - 1, -1, -1):
            if self._grid[row][col] == PieceColor.Empty:
                self._grid[row][col] = color
                return row
        return None 

    def print(self):
        print("Grid:\n")
        for row in range(len(self._grid)):
            view = ""
            for col in range(len(self._grid[row])):
                if self._grid[row][col] == PieceColor.Empty:
                    view += "x"
                elif self._grid[row][col] == PieceColor.Red:
                    view += "R"
                elif self._grid[row][col] == PieceColor.Blue:
                    view += "B"
            print(view)
        print("")
