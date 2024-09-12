import random

# Get the computer's choice
def get_computer_choice():
    """Return a random choice from rock, paper, or scissors"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Determine the winner
def determine_winner(user_choice, computer_choice):
    """Return 'win', 'lose', or 'tie' based on the user's and computer's choices"""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

# Print the result
def print_result(user_choice, computer_choice, result):
    """Print the user's and computer's choices and the result"""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

# Main game loop
def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to make your choice.")
    
    while True:
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, result)
        
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        
        print(f"\nScore: You {user_score} - Computer {computer_score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
