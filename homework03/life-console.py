import curses

from life import GameOfLife
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        horisontal_line = "+"
        for i in range(self.life.cols):
            horisontal_line += "-"
        horisontal_line += "+"

        vertical_line = "|"
        for i in range(self.life.cols):
            vertical_line += " "
        vertical_line += "|"

        screen.addstr(0, 0, horisontal_line)
        for j in range(1, self.life.rows+1):
            screen.addstr(j, 0, vertical_line)
        screen.addstr(j, 0, horisontal_line)
        screen.refresh()

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        pass

    def run(self) -> None:
        screen = curses.initscr()
        # PUT YOUR CODE HERE
        self.draw_borders(screen)
        curses.napms(3000)
        # self.draw_grid(screen)

        curses.endwin()

life = GameOfLife((24, 80))
ui = Console(life)
ui.run()



# import curses
# screen = curses.initscr()
# # Update the buffer, adding text at different locations
# screen.addstr(0, 0, "This string gets printed at position (0, 0)")
# screen.addstr(3, 1, "Try Russian text: Привет")  # Python 3 required for unicode
# screen.addstr(4, 4, "X")
# screen.addch(5, 5, "Y")
#
# # Changes go in to the screen buffer and only get
# # displayed after calling `refresh()` to update
# screen.refresh()
# curses.napms(3000)
# curses.endwin()
