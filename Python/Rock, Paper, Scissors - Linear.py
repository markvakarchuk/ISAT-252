import time
import random

# defining all global variables 
win_streak = 0      # counts how many times the user won
play_again = True   # flag for if another round should be played
game_states = ["rock", "paper", "scissors"]

#printing the welcome message
print("Welcome to Rock, Paper, Scissors, lets play!")
time.sleep(0.5)
input("Press Enter to continue... \n")
# this function is promted at the beginning and after every round if the user won
# def play_round():

while play_again:
    # define local variables 
    user_move = input("Enter 'rock','paper', or 'scissors':  ")

    # computers turn to generate move
    comp_move = random.choice(game_states) 

    # see if user won
    # user can win with 3 different combinations
    # 1) Scissors beats Paper5
    # 2) Rock beats Scissors
    # 3) Paper beats Rock

    if comp_move == user_move: # first check if it was a time
        print("Tie!  Go again! \n")
        play_again = True
    elif comp_move == 'paper' and user_move == 'scissors': # check for combo 1
        print("Scissors beats paper! Go again! \n")
        win_streak += 1
        play_again = True
    elif comp_move == 'scissors' and user_move == 'rock': # check for combo 2
        print("Rock beats scissors! Go again! \n")
        win_streak += 1
        play_again = True
    elif comp_move == 'rock' and user_move == 'paper': # check for combo 3
        print("Paper beats rock! Go again! \n")
        win_streak += 1
        play_again = True
    else: # means computer won, print how computer won and end round
        print("\n" + str(comp_move) + " beats your move of " + str(user_move))
        print("Better luck next time! \n")
        play_again = False
    
print("********************************")
print("Win streak: " + str(win_streak))
print("********************************")
print("\n")
print("Thanks for playing!")
print("\n")
print("\n")