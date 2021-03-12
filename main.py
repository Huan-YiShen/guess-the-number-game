#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import time

def main():
    # Intro
    print("Welcome to this simple guess the number game!")
    print("I have thought up a number (0-100) take a guess what it is ;)")
    difficulty = int(input ("what difficulties would you want to play with (1 - easy mode, 2 - hard mode, 3 - RNGesus): "))

    # pick difficulties
    while (difficulty<1 or difficulty>3):
        print ("    OI! there is no difficult", difficulty)
        difficulty = int(input("    try again (1 - easy mode, 2 - hard mode, 3 - RNGesus): "))

    if difficulty == 1:
        count = 10    
    elif difficulty == 2:
        count = 5    
    elif difficulty == 3:
        count = 2    

    # Play the actual game 
    chosenNum = random.randint(0, 100)
    # print(chosenNum)
    guess = -1
    while (count > 0):
        guess = int(input("guess the number: "))

        while (guess<1 or guess>100):
                print ("    OI! that number is not in range!")
                guess = int(input("    try again (input a number between 1-100): "))

        if(guess < chosenNum):
            print("Too Low")
        elif(guess > chosenNum):
            print("Too High")
       
        if(guess == chosenNum):
            print("Nicely Done! You Got My Number")
            time.sleep(2)
            print("... Now give it back")
            break

        count -= 1
        print ("you have", count, "number of guess(es) left")

    if(count == 0):
        print ("Oh no, it looks like you ran out of guesses, better luck next time! (btw the number is", chosenNum, ")")


if "__main__" == __name__:
    main()