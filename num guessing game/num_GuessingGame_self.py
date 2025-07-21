import random

x = True
while x:
    print("Welcome to number guessing game !")
    print("Gues the number between 0 to 100")
    number = random.randint(1,100)
    count = 0
    while True:
        guess = int(input("Enter the number:-"))
        if guess == number:
            print("Your guess is right")
            print(f"Your {count+1} guess is right")
            break
        elif guess < number :
            print("your guess is TOO LOW, Try again")
            count+=1
        elif guess > number :
            print("your guess is TOO HIGH, Try again")
            count+=1
    while True:
        y=(input("Do you want to play again or not enter (yes/no)")).lower()

        if(y=="yes"):
            x=True
            break
        elif(y=="no"):
            x=False
            break
        else:
            print("Enter the value again")
print("GoodBye")