# Improved rock, paper and scissors game with victory count capability.
# Oikantik Nath, Dec 30, 2018


from random import choice

player_win = 0
comp_win = 0
print("This is a basic rock-paper-scissors game.")
win_score = int(input("Enter winning score: "))

while (player_win < win_score and comp_win < win_score) or player_win == comp_win: 
    player1 = input("Player: Make entry: ").lower()
    if player1 == "quit" or player1 == "q":
        break
    comp = choice(["rock", "paper", "scissors"])
    print(f"Computer makes move: {comp}")

    if player1 == comp:
        print("DRAW!!!")
    elif player1 == "rock":
        if comp == "paper":
            print("Computer wins!!!")
            comp_win += 1
        else:
            print("You win!!!")
            player_win += 1
    elif player1 == "paper":
        if comp == "rock":
            print("You win!!!")
            player_win += 1
        else:
            print("Computer wins!!!")
            comp_win += 1
    elif player1 == "scissors":
        if comp == "paper":
            print("You win!!!")
            player_win += 1
        else:
            print("Computer wins!!!")
            comp_win += 1
    else:
        print("Something went wrong! :(")
    print(f"Player score: {player_win}      Computer score: {comp_win}")

print("RESULT:")
if player_win > comp_win:
    print("You won! :)")
else:
    print("You lost! :(")