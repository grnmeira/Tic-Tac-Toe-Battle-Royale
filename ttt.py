import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 150
HEIGHT = 150
MARGIN = 15

BOARD_SIZE = 3

ROW = 1
COL = 2
DIA = 3
RDIA = 4


class Game:
    def __init__(self):
        self.done = False
        self.on_win_screen = False
        self.grid = init_grid(BOARD_SIZE)
        self.player_turn = 1
        self.win_line = ()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)

        # Set the WIDTH and HEIGHT of the screen [WIDTH, HEIGHT]
        screen_size = (510, 510)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("My Game")

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_q)):
                self.done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # clicked_location = (pos[0], pos[1])
                print(pos)
                clicked_col = pos[0] // (MARGIN + WIDTH)
                clicked_row = pos[1] // (MARGIN + HEIGHT)
                # self.grid[clicked_row][clicked_col] = 1
                if self.grid[clicked_row][clicked_col] == 0:
                    self.grid[clicked_row][clicked_col] = self.player_turn
                    
                    self.check_for_win(clicked_row, clicked_col)

                    if self.player_turn == 1:
                        self.player_turn = 2
                    else:
                        self.player_turn = 1


    def check_for_win(self, clicked_row, clicked_col):
        print("Checking for win")
        # Check row
        for col in range(BOARD_SIZE):
            if self.grid[clicked_row][col] != self.player_turn:
                break
            if col == BOARD_SIZE - 1:
                self.win_line = (ROW, clicked_row, col)

        # Check col
        for row in range(BOARD_SIZE):
            if self.grid[row][clicked_col] != self.player_turn:
                break
            if row == BOARD_SIZE - 1:
                self.win_line = (COL, row, clicked_col)

        # Check diag
        if clicked_row == clicked_col:
            for dia in range(BOARD_SIZE):
                if self.grid[dia][dia] != self.player_turn:
                    break
                if dia == BOARD_SIZE - 1:
                    self.win_line = (DIA, dia, dia)

        # Check ainti/reverse diag
        if (clicked_row + clicked_col) == (BOARD_SIZE - 1):
            for dia in range(BOARD_SIZE):
                if self.grid[dia][(BOARD_SIZE-1) - dia] != self.player_turn:
                    break
                if dia == BOARD_SIZE - 1:
                    self.win_line = (RDIA, dia, dia)

        if self.win_line != ():
            print("WINNING LINE: %s" % (self.win_line, ))


    def draw(self):
        fps = self.font.render(str(int(self.clock.get_fps())), True, pygame.Color('grey'))
        #self.screen.blit(fps, (1, 1))
        #pygame.display.update(self.screen.blit(fps, (1, 1)))

        if not self.on_win_screen:

            # Here, we clear the screen to black. Don't put other drawing commands
            # above this, or they will be erased with this command.
            # If you want a background image, replace this clear with blit'ing the
            # background image.
            self.screen.fill(BLACK)

            color = WHITE
            # --- Drawing code should go here
            # pygame.draw.line(screen, WHITE, [0, 0], [0, 0+WIDTH], MARGIN)
            for row in range(BOARD_SIZE):
                for column in range(BOARD_SIZE):
                    if self.grid[row][column] == 1:
                        color = GREEN
                    elif self.grid[row][column] == 2:
                        color = RED
                    else:
                        color = WHITE

                    pygame.draw.rect(
                            self.screen,
                            color,
                            [(MARGIN+WIDTH) * column + MARGIN,  # left
                                ((MARGIN + HEIGHT) * row) + MARGIN,  # top
                                WIDTH,                          # WIDTH
                                HEIGHT])                        # HEIGHT

            if self.win_line != ():
                self.display_win_line()
            pygame.display.flip()
        pygame.display.update(self.screen.blit(fps, (1, 1))) # TODO keep drawing fps updates but not rest of screen


    def display_win_line(self):
        print("Displaying winning line: %s" % (self.win_line, ))
        if (self.win_line[0]) == ROW:
            print("Winning line is a row")
            pygame.draw.line(
                    self.screen,
                    BLACK,
                    [
                        0, 
                        (MARGIN + HEIGHT//2) + (MARGIN + HEIGHT) * self.win_line[1]
                    ],
                    [
                        (MARGIN+HEIGHT)*BOARD_SIZE + MARGIN,
                        (MARGIN + HEIGHT//2) + (MARGIN + HEIGHT) * self.win_line[1]
                    ],
                    50)
        if (self.win_line[0]) == COL:
            print("Winning line is a column")
            pygame.draw.line(
                    self.screen,
                    BLACK,
                    [
                        (MARGIN + WIDTH//2) + (MARGIN + WIDTH) * self.win_line[2], 
                        0
                    ],
                    [   
                        (MARGIN + WIDTH//2) + (MARGIN + WIDTH) * self.win_line[2], 
                        (MARGIN+HEIGHT)*BOARD_SIZE + MARGIN
                    ],
                    50)
        if (self.win_line[0]) == DIA:
            print("Winning line is a diagonal")
            pygame.draw.line(
                    self.screen,
                    BLACK,
                    [0, 0],
                    [
                        (MARGIN + WIDTH)*BOARD_SIZE + MARGIN, 
                        (MARGIN + HEIGHT)*BOARD_SIZE + MARGIN
                    ],
                    50)
        if (self.win_line[0]) == RDIA:
            print("Winning line is a reverse diagonal")
            pygame.draw.line(
                    self.screen,
                    BLACK,
                    [
                        0, (MARGIN + HEIGHT)*BOARD_SIZE + MARGIN
                    ],
                    [    
                        (MARGIN + WIDTH)*BOARD_SIZE + MARGIN, 0
                    ],
                    50)

        self.on_win_screen = True


def init_grid(size):
    # --- Create grid of numbers
    grid = []
    # Loop for each row
    for row in range(size):
        # For each row, create a list that will represent an entire row
        grid.append([])
        # Loop for each column
        for column in range(size):
            # Add the number zero to the current row
            grid[row].append(0)
    return grid


def main():
    playGame()


def playGame():
    game = Game()

    # Loop until the user clicks the close button.

    # Used to manage how fast the screen updates

    # -------- Main Program Loop -----------
    while not game.done:
        # --- Main event loop
        game.process_events()
        game.draw()

        # --- Limit to 60 frames per second
        game.clock.tick(60)

    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    main()
