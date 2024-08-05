import random

# Initialize scores and wins
player_score = 0
computer_score = 0
player_wins = 0
computer_wins = 0

# Function to take the user input and randomly generate the computer input using the random module
def playerinput():
    choice = input("Rock, paper, scissors or exit: ")
    if choice.lower() == 'exit':  # Allow the player to exit the game
        return None
    computer_choice = random.choice(['rock', 'paper', 'scissors'])  # Randomly generate the computer's choice
    return {
        'player': choice.lower(),
        'computer': computer_choice
    }

# Function to determine the winner of a round
def winner(player_choice, computer_choice):
    global player_score, computer_score, player_wins, computer_wins
    if (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
        player_score += 1
        player_wins += 1
        return f"Player wins this round! Current score: Player - {player_score}, Computer - {computer_score}"
    elif (computer_choice == 'rock' and player_choice == 'scissors') or (computer_choice == 'paper' and player_choice == 'rock') or (computer_choice == 'scissors' and player_choice == 'paper'):
        computer_score += 1
        computer_wins += 1
        return f"Computer wins this round! Current score: Player - {player_score}, Computer - {computer_score}"
    else:
        return "It's a tie!"

# Main loop to play the game continuously
while True:
    player_choice = playerinput()
    if player_choice is None:  # Exit the game if the player chooses to exit
        print("Thanks for playing! Goodbye!")
        break
    computer_choice = player_choice['computer']
    result = winner(player_choice['player'], computer_choice)
    print(result)
    
    # Check if player or computer has reached 5 wins
    if player_wins == 5:
        print("Player wins the game! \n =>computer : {computer_wins} player : {player_wins}")
        break
    elif computer_wins == 5:
        print("Computer wins the game! \n =>computer : {computer_wins} player : {player_wins}")
       
        break
