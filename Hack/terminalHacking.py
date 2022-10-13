# Project made by Eoin Darcy following Tutorials and Guidelines from "The Big Book of Small Python Projects" - By Al Sweigart

import random, sys

# Create Constants
# Random Characters to Space out Words
GARBAGE_CHARS =  '~!@#$%^&*()_+-={}[]|;:,.<>?/'

# Load the WORDS list from the text file
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
    for i in range(len(WORDS)):
        # Convert each word to uppercase and remove the trailing newline
        WORDS[i] = WORDS[i].strips().upper()

def main():
    input('Press Enter to Begin..')
    gameWords = getWords()
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)

    print(computerMemory)
    # Start at 4 Tries
    for triesRemaining in range(4, 0, -1):
        playerMove = askForPlayerGuess(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('A C C E S S   G R A N T E D')
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('Access Denied ({}/7 correct)'.format(numMatches))
    print('Out of Tries. Secret Password was {}.'.format(secretPassword))

def getWords():
# Return 12 Potential Words
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # Find two more words; these have zero matching letters
    # We use "< 3" because the secret password is already in words
    while len(words) < 3:
        randomWord = getOneWordException(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)

    # Find two words that have 3 matching letters (But Limit to 500 incase none can be found)
    for i in range(500):
        if len(words) == 5:
            break # 5 Words found, Break out of Loop

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # Find at least seven words that have at least one matching letter (But Limit to 500 incase none can be found)
    for i in range(500):
        if len(words) == 12:
            break # 7 Words found, Break out of Loop

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
            words.append(randomWord)

    # Add any random words needed to get 12 words total
    while len(words) < 12:
        randomWord = getOneWordsExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words

def getOneWordExcept(blocklist=None):
    # Returns a random word from WORDS that isnt in blocklist
    if blocklist == None:
        blocklist = []

    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord

def numMatchingLetters(word1, word2):
    # Returns  the number of matching letters in these two words
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches

def getComputerMemoryString(words):
    # Pick one line per word to contain a word. 16 Lines, split in 2 Columns
    linesWithWords = random.sample(range(16 * 2), len(words))
    # The starting memory address
    memoryAddress = 16 * random.randint(0, 4000)

    # Create the Memory String
    computerMemory = [] # Will contain 16 strings
    nextWord = 0 # The index in words of the word to put into a line
    for lineNum in range(16): # The Memory has 16 lines
        # Create a Half Line of Garbage Characters
        leftHalf = ''
        rightHalf = ''
        for j in range(16):
            leftHalf += random.choice(GARBAGE_CHARS)
            rightHalf += random.choice(GARBAGE_CHARS)

        # Fill in the Password from Words
        if lineNum in linesWithWords:
            # Find a random place in the half line to insert the word
            insertionIndex = random.randint(0, 9)
            # Insert the Word:
            leftHalf = (leftHalf[:insertionIndex] + words[nextWord] + leftHalf[insertionIndex + 7:])
            nextWord += 1 # Update the Word to put in the Half Line

        if lineNum + 16 in linesWithWords:
            # Find a random place in the half line to insert the word
            insertionIndex = random.randint(0, 9)
            # Insert the Word:
            rightHalf = (rightHalf[:insertionIndex] + words[nextWord] + rightHalf[insertionIndex + 7:])
            nextWord += 1  # Update the Word to put in the Half Line

        computerMemory.append('Ox' + hex(memoryAddress)[2:].zfill(4) + ' ' + leftHalf + ' ' + 'Ox' + hex(memoryAddress + (16*16))[2:].zfill(4) + ' ' + rightHalf)
        memoryAddress += 16 # Jump from, say, 0xe680 to 0xe690

        # Each String in Computer Memory list is joined into one large
        # String to Return
        return '\n'.join(computerMemory)

def askForPlayerGuess(words, tries):
    while True:
        print('Enter Password: ({} tries remaining)'.format(tries))
        guess = input('> ').upper()
        if guess in words:
            return guess
        print('That is not one of the possible Passwords Listed above..')
        print('Try Entering "{}" or "{}".'.format(words[0], words[1]))

# If the Program was Run(Instead of Imported), run the game
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() # When Ctrl - C is Pressed, end the Program