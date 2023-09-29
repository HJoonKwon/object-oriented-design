from collections import deque
from player import Player
from grid import Grid, PieceColor


class Game:
    def __init__(self, grid: Grid, rounds_to_win: int, num_connects_to_win: int):
        self._grid = grid
        self._rounds_to_win = rounds_to_win
        self._num_connects_to_win = num_connects_to_win
        self._players = [
            Player("Player 1", PieceColor.Red),
            Player("Player 2", PieceColor.Blue),
        ]
        self._scores = {player.get_name(): 0 for player in self._players}

    def play_game(self):
        max_score = 0
        while max_score < self._rounds_to_win:
            winner = self.play_round()
            if winner is not None:
                self._scores[winner.get_name()] += 1
                print(f"current score: {self._scores}")
                if self._scores[winner.get_name()] >= max_score:
                    max_score = self._scores[winner.get_name()]
                if max_score >= self._rounds_to_win:
                    print(f"{winner.get_name()} win the game! Congrats!")
                    break

    def play_round(self):
        while True:
            for player in self._players:
                self.play_turn(player)
                if self.check_win(player):
                    print(f"{player.get_name()} win this round!")
                    self._grid.init_grid()
                    return player
            if self.check_draw():
                print(f"Draw!")
                self._grid.init_grid()
                return None

    def play_turn(self, player):
        self._grid.print()
        while True:
            col = int(
                input(
                    f"Enter column to place a piece on between {0} and {self._grid.get_cols()-1} \n"
                )
            )
            if self._grid.set_piece(col, player.get_color()):
                self._grid.print()
                break
            else:
                print("You cannot place a piece here")
                self._grid.print()

    def is_connected(self, row, col, color):
        if (
            row < 0
            or row >= self._grid.get_rows()
            or col < 0
            or col >= self._grid.get_cols()
            or self._grid.get_piece(row, col) != color
        ):
            return False
        else:
            return True

    def check_draw(self):
        for row in range(self._grid.get_rows()):
            for col in range(self._grid.get_cols()):
                if self._grid.get_piece(row, col) == PieceColor.Empty:
                    return False
        return True

    def check_win(self, player):
        # check vertical
        for col in range(self._grid.get_cols()):
            cnt = 0
            for row in range(self._grid.get_rows()):
                if self._grid.get_piece(row, col) == player.get_color():
                    cnt += 1
                else:
                    cnt = 0
                if cnt >= self._num_connects_to_win:
                    return True

        # check horizontal
        for row in range(self._grid.get_rows()):
            cnt = 0
            for col in range(self._grid.get_cols()):
                if self._grid.get_piece(row, col) == player.get_color():
                    cnt += 1
                else:
                    cnt = 0
                if cnt >= self._num_connects_to_win:
                    return True

        # check diagonal
        # (0,0), (1,1), (2,2), ... ,
        # (0,1), (1,2), (2,3), ... ,
        # (0,col-1), (1, col)
        # (0, col)
        for col in range(self._grid.get_cols()):
            row = 0
            cnt = 0
            while row < self._grid.get_rows() and col < self._grid.get_cols():
                if self._grid.get_piece(row, col) == player.get_color():
                    cnt += 1
                else:
                    cnt = 0
                if cnt >= self._num_connects_to_win:
                    return True
                row += 1
                col += 1

        # (1, 0), (2, 1), (3, 2), ...
        # (2, 0), (3, 2), (4, 3), ...
        # (row-1, 0), (row, 1)
        # (row, 0)

        for row in range(1, self._grid.get_rows()):
            col = 0
            cnt = 0
            while row < self._grid.get_rows() and col < self._grid.get_cols():
                if self._grid.get_piece(row, col) == player.get_color():
                    cnt += 1
                else:
                    cnt = 0
                if cnt >= self._num_connects_to_win:
                    return True
                row += 1
                col += 1

        # check reverse diagnoal
        # (0, 0)
        # (0, 1), (1, 0)
        # (0, 2), (1, 1), (1, 0)
        # (0, col), (1, col-1), ...

        # (1, col), (2, col-1), ...
        # (2, col), (3, col-1), ...
        # (row-1, col), (row, col-1)
        # (row, col)

        for col in range(self._grid.get_cols()):
            row = 0
            cnt = 0
            while row < self._grid.get_rows() and col >= 0:
                if self._grid.get_piece(row, col) == player.get_color():
                    cnt += 1
                else:
                    cnt = 0
                if cnt >= self._num_connects_to_win:
                    return True
                row += 1
                col -= 1

        for row in range(1, self._grid.get_rows()):
            col = self._grid.get_cols() - 1
            cnt = 0
            while row < self._grid.get_rows() and col >= 0:
                if self._grid.get_piece(row, col) == player.get_color():
                    cnt += 1
                else:
                    cnt = 0
                if cnt >= self._num_connects_to_win:
                    return True
                row += 1
                col -= 1

        return False
