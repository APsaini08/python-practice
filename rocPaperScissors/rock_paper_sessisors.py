import random

def get_winner(player, computer):
    """Return result based on choices."""
    if player == computer:
        return "draw"
    winning_cases = {
        "rock": "scissors",   # Rock beats Scissors
        "paper": "rock",      # Paper beats Rock
        "scissors": "paper"   # Scissors beats Paper
    }
    return "player" if winning_cases[player] == computer else "computer"

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    print("=== Welcome to Rock Paper Scissors! ===")
    print("Type 'exit' anytime to quit.\n")

    while True:
        player = input("Enter your choice (rock, paper, scissors): ").lower()

        if player == "exit":
            print("\nThanks for playing!")
            break

        if player not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        result = get_winner(player, computer)

        if result == "draw":
            print("It's a DRAW!")
        elif result == "player":
            print("You WIN this round!")
            player_score += 1
        else:
            print("You LOSE this round!")
            computer_score += 1

        # Show the score
        print(f"Score: You {player_score} - {computer_score} Computer\n")

if __name__ == "__main__":
    play_game()
