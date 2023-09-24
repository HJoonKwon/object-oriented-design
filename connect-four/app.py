from game import Game
from grid import Grid
from player import Player

if __name__ == "__main__":
    grid = Grid(5, 7)
    game = Game(grid, 2, 3)

    game.play_game()
