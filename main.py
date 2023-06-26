import pygame
import random
pygame.init()

class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.blockSize = 30
        self.rect = pygame.Rect(self.x, self.y, self.blockSize, self.blockSize)

    def draw(self):
        pygame.draw.rect(scr, self.color, self.rect, 19, 5)
        pygame.draw.rect(scr, 'black', self.rect, 1, 5)


class Figure:
    def __init__(self, x, y):
        color = random.choice(['red', 'green', 'blue', 'yellow'])
        self.type = random.choice(['l', 'i', 's', 'r'])
        self.x = x
        self.y = y
        if self.type == 'l':
            self.blocks = [Block(self.x, self.y, color), Block(self.x, self.y+30, color),
                           Block(self.x, self.y + 60, color), Block(self.x + 30, self.y + 60, color)]
        elif self.type == 'i':
            self.blocks = [Block(self.x, self.y, color), Block(self.x, self.y + 30, color),
                            Block(self.x, self.y + 60, color), Block(self.x, self.y + 90, color)]
        elif self.type == 's':
            self.blocks = [Block(self.x, self.y, color), Block(self.x + 30, self.y, color),
                           Block(self.x, self.y + 30, color), Block(self.x - 30, self.y + 30, color)]
        elif self.type == 'r':
            self.blocks = [Block(self.x, self.y, color), Block(self.x + 30, self.y, color),
                           Block(self.x, self.y + 30, color), Block(self.x + 30, self.y + 30, color)]

    def draw(self):
        for block in self.blocks:
            block.draw()

    def move(self, direction='down'):
        if direction == 'down':
            for block in self.blocks:
                block.rect.y += 1
        elif direction == 'left':
            for block in self.blocks:
                block.rect.x -= block.blockSize
        elif direction == 'right':
            for block in self.blocks:
                block.rect.x += block.blockSize
        elif direction == 'faster_down':
            for block in self.blocks:
                block.rect.y += block.blockSize


def checkColision(figure):
    for block in figure.blocks:
        if block.rect.colliderect(bottom_barier):
            return True
        if block.rect.collideobjects(fallen_blocks):
            return True

def checkFilling(blocks):
    x = width
    y = height
    while y != 0:
        count = 0
        while x != 0:
            for block in blocks:
                if block.rect.collidepoint(x+1, y-28):
                    count += 1
            if count == 10:
                for block in blocks:
                    if block.rect.collidepoint(x+1, y-28):
                        blocks.remove(block)
            x -= block_size
        y -= block_size

block_size = 30
width = block_size * 10
height = block_size * 20

clock = pygame.time.Clock()

pygame.mixer.music.load('bg_music.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

fall_sound = pygame.mixer.Sound('fall_sound.mp3')
fall_sound.set_volume(0.1)

scr = pygame.display.set_mode((width, height))
bgColor = 'black'

cur_figure = Figure(width/2 - block_size, 0)
fallen_blocks = []

bottom_barier = pygame.Rect(0, height, width, 1)
left_barier = pygame.Rect(-1, 0, 1, height)
right_barier = pygame.Rect(width, 0, 1, height)

GameOver = False
while not GameOver:

    if checkColision(cur_figure):
        for block in cur_figure.blocks:
            fallen_blocks.append(block)
            fall_sound.play()
        cur_figure = Figure(width/2 - block_size, 0)
        checkFilling(fallen_blocks)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cur_figure.move('left')
            if event.key == pygame.K_RIGHT:
                cur_figure.move('right')
            if event.key == pygame.K_DOWN:
                cur_figure.move('faster_down')
    scr.fill(bgColor)

    cur_figure.move()

    cur_figure.draw()
    for block in fallen_blocks:
        block.draw()


    pygame.display.update()
    clock.tick(60)
