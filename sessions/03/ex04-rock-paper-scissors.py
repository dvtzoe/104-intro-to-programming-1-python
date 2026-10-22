player_choice = input("rock, paper, scissors? ")

print("Computer: rock")

if player_choice == "rock":
    print("Draw!")
elif player_choice == "paper":
    print("You win!")
elif player_choice == "scissors":
    print("Computer wins!")
else:
    print("Invalid choice")
