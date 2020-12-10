import pygame
from pygame.locals import *
import sys

from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int=10, speed: int=10) -> None:
        super().__init__(life)

        self.cell_size = cell_size
        self.speed = speed

        self.height = self.life.rows * self.cell_size
        self.width = self.life.cols * self.cell_size

        # Устанавливаем размер окна
        self.screen_size = self.width, self.height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        self.is_paused: bool=False

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height), 1)
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y), 1)

    def draw_grid(self) -> None:
        dark_green = pygame.Color(0, 128, 0)
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                if self.life.curr_generation[i][j] == 1:
                    x = j * self.cell_size
                    y = i * self.cell_size

                    pygame.draw.rect(self.screen, pygame.Color(dark_green),
                                     (x + 1, y + 1, self.cell_size - 1, self.cell_size - 1))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.is_paused = not self.is_paused

        if self.is_paused:
            pygame.draw.circle(self.screen, pygame.Color('red'),
                               (self.height / 2, self.width / 2), 30)
            pygame.time.wait(100)
            self.update()

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        while self.life.is_changing and not self.life.is_max_generations_exceed:
            self.is_paused = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.screen.fill(pygame.Color('white'))
            self.draw_lines()
            self.draw_grid()
            self.life.step()
            self.update()
            # keys = pygame.key.get_pressed()
            # if self.is_paused:
            # while keys[pygame.K_SPACE]:
            #     keys = pygame.key.get_pressed()
            #     pygame.time.wait(1)

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


sys_cols = 0
sys_rows = 0
sys_max_gen = 0
sys_cell = 0
sys_speed = 0
if len(sys.argv) <= 1:
    print("\nВызов программы со стандартными настройками.\nВызовите программу с аргументом --help для помощи.\n")
else:
    for j in range(1, len(sys.argv), 2):
        i = sys.argv[j]
        if i == "--help":
            print('\n   Чтобы установить размер окна воспользуйтесь аргументами --rows <int> --cols <int>\n'
                  '   Чтобы установить максимальное число поколений в игре воспользуйтесь аргументом --max_generations <int>\n'
                  '   Чтобы установить размер клетки воспользуйтесь аргументом --cell <int>\n'
                  '   Чтобы установить скорость игры воспользуйтесь аргументом --speed <int>\n'
                  '   Приятной игры!\n')
            exit(1)
        elif i == "--rows":
            sys_rows = int(sys.argv[j+1])
        elif i == "--cols":
            sys_cols = int(sys.argv[j+1])
        elif i == "--max_generations":
            sys_max_gen = int(sys.argv[j+1])
        elif i == "--cell":
            sys_cell = int(sys.argv[j+1])
        elif i == "--speed":
            sys_speed = int(sys.argv[j+1])
        else:
            print("\nНеверный ключ командной строки: ", i, "\n"
                "Вызовите программу с аргументом --help для помощи.\n")
            exit(1)

life = GameOfLife((24, 80))
if sys_cell == 0:
    sys_cell = 10
if sys_cols == 0:
    sys_cols = 80
if sys_rows == 0:
    sys_rows = 24
if sys_max_gen == 0:
    sys_max_gen = 10
if sys_speed == 0:
    sys_speed = 10

life = GameOfLife((sys_rows, sys_cols), max_generations=sys_max_gen)
ui = GUI(life, cell_size=sys_cell, speed=sys_speed)
ui.run()
