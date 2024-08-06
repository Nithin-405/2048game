import random

class Game:
    def __init__(self):
        self.grid = [[0]*4 for _ in range(4)]
        self.add_number()
        self.add_number()

    def add_number(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def compress(self):
        new_grid = [[0]*4 for _ in range(4)]
        for i in range(4):
            pos = 0
            for j in range(4):
                if self.grid[i][j] != 0:
                    new_grid[i][pos] = self.grid[i][j]
                    pos += 1
        self.grid = new_grid

    def merge(self):
        for i in range(4):
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j+1] and self.grid[i][j] != 0:
                    self.grid[i][j] *= 2
                    self.grid[i][j+1] = 0

    def reverse(self):
        self.grid = [row[::-1] for row in self.grid]

    def transpose(self):
        self.grid = [list(i) for i in zip(*self.grid)]

    def check_empty_cells(self):
        return any(0 in row for row in self.grid)

    def check_game_over(self):
        for i in range(4):
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j+1]:
                    return False
        self.transpose()
        for i in range(4):
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j+1]:
                    self.transpose()
                    return False
        self.transpose()
        return not self.check_empty_cells()

    def play(self):
        while True:
            print('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid]))
            move = input("Enter your move (W/A/S/D): ")
            if move == 'W':
                self.transpose()
                self.compress()
                self.merge()
                self.compress()
                self.transpose()
            elif move == 'A':
                self.compress()
                self.merge()
                self.compress()
            elif move == 'S':
                self.transpose()
                self.reverse()
                self.compress()
                self.merge()
                self.compress()
                self.reverse()
                self.transpose()
            elif move == 'D':
                self.reverse()
                self.compress()
                self.merge()
                self.compress()
                self.reverse()
            else:
                print("Invalid move. Please enter W, A, S or D.")
                continue
            self.add_number()
            if self.check_game_over():
                print("Game Over!")
                break

if __name__ == "__main__":
    game = Game()
    game.play()