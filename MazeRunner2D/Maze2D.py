# mazes generated at https://www.dcode.fr/maze-generator
# Project made by Eoin Darcy following Tutorials and Guidelines from "The Big Book of Small Python Projects" - By Al Sweigart
# Copy txt file name and paste into console to open specified file
import sys, os

# Maze Constants
import sys, os

# Maze file constants:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'
BLOCK = chr(9617)  # Character 9617 is '░'

def displayMaze(maze):
    # Display the maze:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (playerx, playery):
                print(PLAYER, end='')
            elif (x, y) == (exitx, exity):
                print('X', end='')
            elif maze[(x, y)] == WALL:
                print(BLOCK, end='')
            else:
                print(maze[(x, y)], end='')
        print()  # Print a newline after printing the row.

# Get the maze file's filename from the user:
while True:
    print('Enter the filename of the maze (or LIST or QUIT):')
    filename = input('> ')

    # List all the maze files in the current folder:
    if filename.upper() == 'LIST':
        print('Maze files found in', os.getcwd())
        for fileInCurrentFolder in os.listdir():
            if (fileInCurrentFolder.startswith('maze') and
            fileInCurrentFolder.endswith('.txt')):
                print('  ', fileInCurrentFolder)
        continue

    if filename.upper() == 'QUIT':
        sys.exit()

    if os.path.exists(filename):
        break
    print('There is no file named', filename)

# Load the maze from a file:
mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
playerx = None
playery = None
exitx = None
exity = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), 'Invalid character at column {}, line {}'.format(x + 1, y+ 1)
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            playerx, playery = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert playerx != None and playery != None, 'No start in maze file.'
assert exitx != None and exity != None, 'No exit in maze file.'

while True:  # Main game loop.
    displayMaze(maze)

    while True:  # Get user move.
        print('                           W')
        print('Enter direction, or QUIT: ASD')
        move = input('> ').upper()

        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if move not in ['W', 'A', 'S', 'D']:
            print('Invalid direction. Enter one of W, A, S, or D.')
            continue

        # Check if the player can move in that direction:
        if move == 'W' and maze[(playerx, playery - 1)] == EMPTY:
            break
        elif move == 'S' and maze[(playerx, playery + 1)] == EMPTY:
            break
        elif move == 'A' and maze[(playerx - 1, playery)] == EMPTY:
            break
        elif move == 'D' and maze[(playerx + 1, playery)] == EMPTY:
            break

        print('You cannot move in that direction.')

    # Keep moving in this direction until you encounter a branch point.
    if move == 'W':
        while True:
            playery -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery - 1)] == WALL:
                break  # Break if we've hit a wall.
            if (maze[(playerx - 1, playery)] == EMPTY
                or maze[(playerx + 1, playery)] == EMPTY):
                break  # Break if we've reached a branch point.
    elif move == 'S':
        while True:
            playery += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery + 1)] == WALL:
                break  # Break if we've hit a wall.
            if (maze[(playerx - 1, playery)] == EMPTY
                or maze[(playerx + 1, playery)] == EMPTY):
                break  # Break if we've reached a branch point.
    elif move == 'A':
        while True:
            playerx -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx - 1, playery)] == WALL:
                break  # Break if we've hit a wall.
            if (maze[(playerx, playery - 1)] == EMPTY
                or maze[(playerx, playery + 1)] == EMPTY):
                break  # Break if we've reached a branch point.
    elif move == 'D':
        while True:
            playerx += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx + 1, playery)] == WALL:
                break  # Break if we've hit a wall.
            if (maze[(playerx, playery - 1)] == EMPTY
                or maze[(playerx, playery + 1)] == EMPTY):
                break  # Break if we've reached a branch point.

    if (playerx, playery) == (exitx, exity):
        displayMaze(maze)
        print('You have reached the exit! Good job!')
        sys.exit()
