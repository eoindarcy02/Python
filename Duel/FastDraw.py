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
    time.sleep(random.randint(20, 50) / 10.0)  # Will Sleep for Random Seconds Between 20 & 50 Which is then Divided by 10 for ms Conversion
    print('DRAW!')
    drawTime = time.time()
    input()  # This Function call Doesn't return Until ENTER is Pressed
    timeElapsed = time.time() - drawTime

    # IF/ELSE Statements for Input in Before/Loss/Win Case
    if timeElapsed < 0.01:
        # Error Handling for IF Player Presses ENTER BEFORE DRAW! Appears
        print('You Drew Before "DRAW!" Appeared! You Lose')
    elif timeElapsed > 0.3:
        # ELIF Statement for IF Player Presses ENTER AFTER 0.3 Seconds
        timeElapsed = round(timeElapsed, 4)
        print('You Took', timeElapsed, 'Seconds to Draw... Too Slow!')
    else:
        # ELSE Statement for IF Player Presses ENTER BEFORE 0.3 Seconds
        timeElapsed = round(timeElapsed, 4)
        print('You Took ', timeElapsed, 'Seconds to Draw!... You Win!')

    print('Enter QUIT to Stop, or Press ENTER to Play Again')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Thanks for Playing!')
        sys.exit()
