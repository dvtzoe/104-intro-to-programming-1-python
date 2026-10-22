import random

choices = ["rock", "paper", "scissors"]

player_choice = input("rock, paper, scissors? ")

if player_choice not in choices:
    print("Invalid choice")
else:
    computer_choice_index = random.randint(0, 2)
    print(f"Computer: {choices[computer_choice_index]}")

    player_choice_index = choices.index(player_choice)

    index_difference = (computer_choice_index - player_choice_index) % 3

    if index_difference == 0:
        print("Draw!")
    elif index_difference == 1:
        print("Computer wins!")
    else:
        print("You wins!")
