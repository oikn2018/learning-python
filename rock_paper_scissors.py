# This is a basic rock-paper-scissors game.
# Oikantik Nath, Dec 28, 2018
print("This is a basic rock-paper-scissors game.")
player1 = input("Player 1: Make entry: ")
print("***NO CHEATING***\n" * 30)
player2 = input("Player 2: Make entry: ")

if player1 == player2:
    print("DRAW!!!")
elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins!!!")
elif player1 == "rock" and player2 == "scissors":
    print("Player 1 wins!!!")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins!!!")
elif player1 == "paper" and player2 == "scissors":
    print("Player 2 wins!!!")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins!!!")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 wins!!!")
elif player1 == player2:
    print("DRAW!!!")
else:
    print("Something went wrong! :(")