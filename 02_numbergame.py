# Project: Guess the number game between 1 and 10
# concept: while loop

print("---WELCOME TO OUR GUESS THE NUMBER GAME SHOW---")
print("so let's start our game")
num = int(input("Select a number between 1 and 10: "))
while num!=7:
    print("Sorry!! you guessed it wrong.")
    a = int(input("Try again: "))

print("Congratulations!! You are correct.")