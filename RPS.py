import random
rPS = ["ROCK", "PAPER", "SCISSORS"]
def main():
    answer1 = ""
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Welcome to Rock, Paper, Scissors! Please enter one of those options and see if you beat the Computer!")
    print("If you would like to quit the game type 'exit'")
    print("----------------------------")
    answer = input()
    answer = answer.upper()
    if answer != rPS[0] and answer != rPS[1] and answer != rPS[2] and answer != "EXIT":
        while answer1 != rPS[0] and answer1 != rPS[1] and answer1 != rPS[2] and answer1 != "EXIT":
            print("----------------------------")
            print("That is an incorrect choice, try again!")
            answer1 = input()
            answer1 = answer1.upper()
        answer = answer1
    if answer == "EXIT":
        exit()
    answerC = rPS[random.randint(0,2)]
    print(answerC.lower())
    print("----------------------------")
    if answerC == answer:
        print("You Tied!")
    elif answerC == rPS[0]:
        if answer == rPS[1]:
            print("You Won!")
        else:
            print("You Lost!")
    elif answerC == rPS[1]:
        if answer == rPS[0]:
            print("You Lost!")
        else:
            print("You Won!")
    elif answerC == rPS[2]:
        if answer == rPS[0]:
            print("You Won!")
        else:
            print("You Lost!")
while(True):
    main()
