import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    
    # Select difficulty level
    while True:
        level = input("Choose difficulty (easy/medium/hard): ").lower()
        if level == "easy":
            max_num = 50
            lives = 10
            break
        elif level == "medium":
            max_num = 100
            lives = 7
            break
        elif level == "hard":
            max_num = 200
            lives = 5
            break
        else:
            print("Invalid choice. Please type easy, medium, or hard.")
    
    # Generate random number
    number = random.randint(1, max_num)
    attempts = 0

    print(f"I have chosen a number between 1 and {max_num}. You have {lives} chances to guess it!")

    # Guess loop
    while lives > 0:
        try:
            guess = int(input(f"Enter your guess ({lives} lives left): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess == number:
            score = max(100 - (attempts - 1) * 10, 0)  # Decrease score for each wrong attempt
            print(f"🎉 Congratulations! You guessed the number {number} in {attempts} attempts!")
            print(f"Your score: {score}")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        lives -= 1

    if lives == 0:
        print(f"😢 You ran out of lives! The correct number was {number}.")

# Main game loop
while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye! Thanks for playing.")
        break
