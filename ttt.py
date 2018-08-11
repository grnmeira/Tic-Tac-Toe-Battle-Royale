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

pygame.init()

# Set the WIDTH and HEIGHT of the screen [WIDTH, HEIGHT]
size = (510, 510)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --- Create grid of numbers
# Create an empty list
grid = []
# Loop for each row
for row in range(BOARD_SIZE):
    # For each row, create a list that will represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(BOARD_SIZE):
        # Add the number zero to the current row
        grid[row].append(0)

player_turn = 1

# -------- Main Program Loop -----------
win_line = ()
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and (
                event.key == pygame.K_q)):
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # clicked_location = (pos[0], pos[1])
            print(pos)
            clicked_col = pos[0] // (MARGIN + WIDTH)
            clicked_row = pos[1] // (MARGIN + HEIGHT)
            # grid[clicked_row][clicked_col] = 1
            if grid[clicked_row][clicked_col] == 0:
                grid[clicked_row][clicked_col] = player_turn

                # Check row
                for col in range(BOARD_SIZE):
                    if grid[clicked_row][col] != player_turn:
                        break
                    if col == BOARD_SIZE - 1:
                        win_line = (ROW, clicked_row, col)

                # Check col
                for row in range(BOARD_SIZE):
                    if grid[row][clicked_col] != player_turn:
                        break
                    if row == BOARD_SIZE - 1:
                        win_line = (COL, row, clicked_col)

                # Check diag
                if clicked_row == clicked_col:
                    for dia in range(BOARD_SIZE):
                        if grid[dia][dia] != player_turn:
                            break
                        if dia == BOARD_SIZE - 1:
                            win_line = (DIA, dia, dia)

                # Check ainti/reverse diag
                if (clicked_row + clicked_col) == (BOARD_SIZE - 1):
                    for dia in range(BOARD_SIZE):
                        if grid[dia][(BOARD_SIZE-1) - dia] != player_turn:
                            break
                        if dia == BOARD_SIZE - 1:
                            win_line = (RDIA, dia, dia)

                print(win_line)

                if player_turn == 1:
                    player_turn = 2
                else:
                    player_turn = 1

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    color = WHITE
    # --- Drawing code should go here
    # pygame.draw.line(screen, WHITE, [0, 0], [0, 0+WIDTH], MARGIN)
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = RED
            else:
                color = WHITE

            pygame.draw.rect(
                    screen,
                    color,
                    [(MARGIN+WIDTH) * column + MARGIN,  # left
                        ((MARGIN + HEIGHT) * row) + MARGIN,  # top
                        WIDTH,                          # WIDTH
                        HEIGHT])                        # HEIGHT

    if win_line != ():
        if (win_line[0]) == ROW:
                pygame.draw.line(
                        screen,
                        BLACK,
                        [
                            0, 
                            (MARGIN + HEIGHT//2) + (MARGIN + HEIGHT) * win_line[1]
                        ],
                        [
                            (MARGIN+HEIGHT)*BOARD_SIZE + MARGIN,
                            (MARGIN + HEIGHT//2) + (MARGIN + HEIGHT) * win_line[1]
                        ],
                        50)
        if (win_line[0]) == COL:
                pygame.draw.line(
                        screen,
                        BLACK,
                        [
                            (MARGIN + WIDTH//2) + (MARGIN + WIDTH) * win_line[2], 
                            0
                        ],
                        [   
                            (MARGIN + WIDTH//2) + (MARGIN + WIDTH) * win_line[2], 
                            (MARGIN+HEIGHT)*BOARD_SIZE + MARGIN
                        ],
                        50)
        if (win_line[0]) == DIA:
                pygame.draw.line(
                        screen,
                        BLACK,
                        [0, 0],
                        [
                            (MARGIN + WIDTH)*BOARD_SIZE + MARGIN, 
                            (MARGIN + HEIGHT)*BOARD_SIZE + MARGIN
                        ],
                        50)
        if (win_line[0]) == RDIA:
                pygame.draw.line(
                        screen,
                        BLACK,
                        [
                            0, (MARGIN + HEIGHT)*BOARD_SIZE + MARGIN
                        ],
                        [    
                            (MARGIN + WIDTH)*BOARD_SIZE + MARGIN, 0
                        ],
                        50)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
