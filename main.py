import pygame
import random
pygame.init()

window_weight = 800
window_height = 600

BLOCK_SIZE = 30
GRID_WIDTH = window_weight // BLOCK_SIZE
GRID_HEIGHT = window_height // BLOCK_SIZE
class Block():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self,surface):
        pygame.draw.rect(surface, self.color, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE,))

class GameWindow:
    def __init__(self):
        self.surface=pygame.display.set_mode((window_weight, window_height))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x] is not None:
                    self.grid[y][x].draw(self.surface)
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.surface.fill("black")
            self.draw_grid()
            pygame.display.flip()
            self.clock.tick(60)

game_window = GameWindow()
game_window.run()