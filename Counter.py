# Project made by Eoin Darcy following Tutorials and Guidelines from "The Big Book of Small Python Projects" - By Al Sweigart


# While Loop to Input Starting No.
while True:
    response = input('Enter a Starting Number: ')
    if response == '':
        response = '0'  # Begin at 0 IF No Number Stated
        break
    if response.isdecimal():  # Error Check to allow for Only Integers to be Input
        break
    print('Number Must be >= 0')
start = int(response)

# While Loop to Input Range of Numbers
while True:
    response = input('Enter how many Numbers to Display: ')
    if response == '':  # Display 1000 Steps IF No Number Stated
        response == '1000'
        break
    if response.isdecimal():  # Error Check to allow for Only Integers to be Input
        break
    print('Please Enter a Number: ')
amount = int(response)

for number in range(start, start + amount):  # Main Loop
    # Convert to Hex/Bin and Remove the Prefix
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]

    print('DEC:  ', number, ' HEX:  ', hexNumber, ' BIN:  ', binNumber)