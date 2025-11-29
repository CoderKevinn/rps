import random

def play_rps_game():
    """
    Runs a single round of Rock Paper Scissors against the computer.
    """
    options = ["rock", "paper", "scissors"]
    
    computer_choice = random.choice(options)
    
    # Get 
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    # Validate the user input
    if user_choice not in options:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == "rock"
    "" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win! 🎉")
    else:
        print("You lose! 😢")

# Run the game when the script is executed
if __name__ == "__main__":
    play_rps_game()
