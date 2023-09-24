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
                row, col = self.play_turn(player)
                if self.check_win(player):
                    print(f"{player.get_name()} win this round!")
                    self._grid.init_grid()
                    return player

    def play_turn(self, player):
        self._grid.print()
        col = int(
            input(
                f"Enter column to place a piece on between {0} and {self._grid.get_cols()-1} \n"
            )
        )
        row = self._grid.set_piece(col, player.get_color())
        self._grid.print()
        return (row, col)

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

    def bfs(self, visited, row, col, color):
        if (row, col) in visited or self._grid.get_piece(row, col) != color:
            return 0  # already visited

        color = self._grid.get_piece(row, col)

        queue = deque()
        queue.append((row, col))
        num_connects = 0
        while len(queue) > 0:
            row, col = queue.popleft()
            visited.add((row, col))
            num_connects += 1
            neighbors = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
            for neighbor in neighbors:
                row_togo, col_togo = neighbor
                if (
                    self.is_connected(row_togo, col_togo, color)
                    and (row_togo, col_togo) not in visited
                ):
                    queue.append((row_togo, col_togo))
        return num_connects

    def check_win(self, player):
        visited = set()
        for row in range(self._grid.get_rows()):
            for col in range(self._grid.get_cols()):
                num_connects = self.bfs(visited, row, col, player.get_color())
                if num_connects == self._num_connects_to_win:
                    return True
        return False
