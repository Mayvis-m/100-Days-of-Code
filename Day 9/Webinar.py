# print("Hello, world!")
# print("WGUCC is awesome!")

# name = input("My name is: ")

# print("Your name is " + name)

# numNa = 0 
# while numNa <16:
#     print("Na")
#     numNa = numNa + 1
# print("Batman!")

# a = 3
# if a > 4:
#     print("Yes it's larger")
# elif a < 4:
#     print("No, it's smaller")
# else:
#     print("maybe they're equal")

# rock, paper, scissors game
import random

wins = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

choices = ["rock", "paper", "scissors"]

human_turn = input("enter your choice:")
computer_turn = random.choice(choices)

print("you chose: " + human_turn)
print("computer chose: " + computer_turn)

if human_turn == computer_turn:
    print("it's a tie!")
elif wins[human_turn] != computer_turn:
    print("computer wins!")
else:
    print("human wins!")

