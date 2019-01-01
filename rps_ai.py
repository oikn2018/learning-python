# This is a basic rock-paper-scissors game played against computer.
# Oikantik Nath, Dec 29, 2018

from random import choice

print("This is a basic rock-paper-scissors game.")
player1 = input("Player: Make entry: ").lower()
comp = choice(["rock", "paper", "scissors"])
print(f"Computer makes move: {comp}")

if player1 == comp:
    print("DRAW!!!")
elif player1 == "rock":
    if comp == "paper":
        print("Computer wins!!!")
    else:
        print("You win!!!")
elif player1 == "paper":
    if comp == "rock":
        print("You win!!!")
    else:
        print("Computer wins!!!")
elif player1 == "scissors":
    if comp == "paper":
        print("You win!!!")
    else:
        print("Computer wins!!!")
else:
    print("Something went wrong! :(")