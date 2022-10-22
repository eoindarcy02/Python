# Project made by Eoin Darcy following Tutorials and Guidelines from "The Big Book of Small Python Projects" - By Al
# Sweigart

import random
import sys
import time

print('When you see "DRAW!" you have 0.3 Seconds to Press ENTER')
print()
print('You Lose if ENTER is Pressed before "DRAW" Appears')
print()
input('Press ENTER to Begin.....')

while True:
    print()
    print("It's High Noon..")
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW!')
    drawTime = time.time()
    input()  # This Function call Doesn't return Until ENTER is Pressed
    timeElapsed = time.time() - drawTime

    # IF/ELSE Statements for Input in Before/Loss/Win Case
    if timeElapsed < 0.01:
        # Error Handling for IF Player Presses ENTER Before DRAW! Appears
        print('You Drew Before "DRAW!" Appeared! You Lose')
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 4)
        print('You Took', timeElapsed, 'Seconds to Draw... Too Slow!')
    else:
        timeElapsed = round(timeElapsed, 4)
        print('You Took ', timeElapsed, 'Seconds to Draw!... You Win!')

    print('Enter QUIT to Stop, or Press ENTER to Play Again')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Thanks for Playing!')
        sys.exit()

