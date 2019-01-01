# Guessing game to guess a number to match with a randomly-generated number.
# Oikantik Nath, Dec 30, 2018

from random import randint

r_num = randint(1, 10)
num = int(input("Enter a number between 1 and 10:"))
while True:
    if num < r_num:
        print("Too low! Try again.")
    elif num > r_num:
        print("Too high! Try again.")
    else:
        print("That's it! Well done!")
        ch = input("Do you want to play again(y/n)?")
        r_num = randint(1, 10)
        if ch == "n":
            break
    num = int(input("Enter a number between 1 and 10:"))