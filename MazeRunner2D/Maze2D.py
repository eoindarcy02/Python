# mazes generated at https://www.dcode.fr/maze-generator
# Project made by Eoin Darcy following Tutorials and Guidelines from "The Big Book of Small Python Projects" - By Al Sweigart
# Copy txt file name and paste into console to open specified file
import sys, os

# Maze Constants
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'
BLOCK = chr(9617) # Character 9617 is '░'

def displayMaze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (playerx, playery):
                print(PLAYER, end = '')
            elif (x, y) == (exitx, exity):
                print('X', end='')
            elif maze[(x, y)] == WALL:
                print(BLOCK, end='')
            else:
                print(maze[(x, y)], end='')
            print() # Print a newline after printing the row.

# Get Maze Files from User
while True:
    print('Enter the Filename of the Maze (or LIST or QUIT): ')
    filename = input('- ')
    # List All Maze Files in Folder
    if filename.upper() == 'LIST':
        print('Maze Files Found in: ', os.getcwd())
        for fileInCurrentFolder in os.listdir():
            if (fileInCurrentFolder.startswith('maze') and fileInCurrentFolder.endswith('.txt')):
                print(' ', fileInCurrentFolder)
                continue
    if filename.upper() == 'QUIT':
        sys.exit()
    if os.path.exists(filename):
        break

# Load the Maze from a File
mazeFile = open(filename)
maze = {}
lines = mazeFile.readline()
playerx = None
playery = None
exitx = None
exity = None
y = 0
for line in lines:
    WIDTH = len(line.rsplit())
    for x, character in enumerate(line.rsplit()):
        assert character in (WALL, EMPTY, START, EXIT), 'Invalid Character at Column {}, Line {}'.format(x + 1, y + 1)
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            playerx, playery = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
        y + 1
    HEIGHT = y

    assert playerx != None and playery != None, 'No Start in Maze File'
    assert exitx != None and exity != None, 'No Exit in Maze File'

while True:
    displayMaze(maze) # Main Game Loop

    while True:
        print('W')
        print('Enter Direction, or QUIT: ASD')
        move = input('- ').upper()

        if move == 'QUIT':
            print('Thanks for Playing!')
            sys.exit

        if move not in ['W', 'A', 'S', 'D']:
            print('Invalid Direction. Enter W, A, S, or D')
            continue
        # Check to see if Player can move in Specified Direction
        if move == 'W' and maze[(playerx, playery - 1)] == EMPTY:
            break
        if move == 'S' and maze[(playerx, playery + 1)] == EMPTY:
            break
        if move == 'A' and maze[(playerx, playery - 1)] == EMPTY:
            break
        if move == 'D' and maze[(playerx, playery + 1)] == EMPTY:
            break
        print('You Cannot move in that Direction')

    # Keep Moving until Branch Point is Encountered
    if move == 'W':
        while True:
            playery -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery - 1)] == WALL:
                break # Wall Hit
            if (maze[(playerx - 1, playery)] == EMPTY
                or maze[(playerx + 1, playery)] == EMPTY):
                break
    elif move == 'S':
        while True:
            playery += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery + 1)] == WALL:
                break
            if (maze[(playerx - 1, playery)] == EMPTY
                    or maze[(playerx + 1, playery)] == EMPTY):
                break
    elif move == 'A':
        while True:
            playery -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery - 1)] == WALL:
                break
            if (maze[(playerx - 1, playery)] == EMPTY
                    or maze[(playerx + 1, playery)] == EMPTY):
                break
    elif move == 'D':
        while True:
            playery += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery + 1)] == WALL:
                break
            if (maze[(playerx - 1, playery)] == EMPTY
                    or maze[(playerx + 1, playery)] == EMPTY):
                break

    if (playerx, playery) == (exitx, exity):
        displayMaze(maze)
        print('Finished!')
        sys.exit()