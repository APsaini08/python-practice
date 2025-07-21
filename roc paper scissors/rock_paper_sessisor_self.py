import random

print("Welcome to Rock paper Sessisor")
print("enter 'exit' if you don't want to play")
choices = ["rock", "paper", "sessisors"]
while True:

    ans = input("Enter your choice like rock,paper,sessisors:-").lower()
    if(ans == "exit"):
        print("GoodBye")
        break
    val = random.choice(choices)
    if(val == ans):
        print("DRAW : You both has choosen the same option")
    elif(val == "rock" and ans == "paper"):
        print("YOU WIN")
    elif(val == "rock" and ans == "sessisors"):
        print("YOU LOOSE")
    elif(val == "paper" and ans == "rock"):
        print("YOU LOOSE")
    elif(val == "paper" and ans == "sessisors"):
        print("YOU WIN")
    elif(val == "sessisors" and ans == "rock"):
        print("YOU WIN")
    elif(val == "sessisors" and ans == "paper"):
        print("YOU LOOSE")
    else:
        print("Enter the valid input like:- rock, paper, sessisors")