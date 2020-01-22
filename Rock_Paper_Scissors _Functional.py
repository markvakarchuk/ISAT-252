import time
import random

# defining all global variables 
win_streak = 0      # counts how many times the user won
play_again = True   # flag for if another round should be played
game_states = ["rock", "paper", "scissors"]
id = 0

rounds = []

#printing the welcome message
print("Welcome to Rock, Paper, Scissors, lets play!")
time.sleep(0.5)
input("Press Enter to continue... \n")


class round():
    def __init__(self, id, comp_move, user_move):
        self.id = id
        self.comp = comp_move
        self.user = user_move


def determine_winner(comp_move, user_move):
    global id
    global win_streak
    global play_again

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
    
    id += 1

    round_played =  round (id, comp_move, user_move)
    rounds.append(round_played)
    return play_again, win_streak

while play_again:
    user_move = input("Enter 'rock','paper', or 'scissors':  ")
    comp_move = random.choice(game_states)
    #comp_move = "scissors" # for practice so user wins everytime 
    determine_winner(comp_move, user_move)

for i in range(len(rounds)):
    round = rounds[i]
    print("\n")
    print("Round: " + str(round.id))
    print("User move: " + str(round.user))
    print("Computer move: " + str(round.comp))
    
print("\n Win Streak: " + str(win_streak))