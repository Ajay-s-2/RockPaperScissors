import random

# Function to take the user input and randomly generate the computer input using the random module
def playerinput():
    player = input("Enter your choice: rock, paper, or scissors (or type 'exit' to quit): ").lower()
    if player == 'exit':
        return None
    option = ["rock", "paper", "scissors"]
    computer = random.choice(option)  # Computer randomly generates the input from the list
    choices = {"player": player, "computer": computer}
    return choices

# Function to find the winner
def winner(player, computer):
    print(f"Player chose {player} and computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Player wins!"
        else:
            return "Computer wins!"
    elif player == "paper":
        if computer == "rock":
            return "Player wins!"
        else:
            return "Computer wins!"
    elif player == "scissors":
        if computer == "paper":
            return "Player wins!"
        else:
            return "Computer wins!"

# Main loop to play the game continuously
while True:
    choices = playerinput()
    if choices is None:
        print("Thanks for playing! Goodbye!")
        break
    result = winner(choices["player"], choices["computer"])
    print(result)

