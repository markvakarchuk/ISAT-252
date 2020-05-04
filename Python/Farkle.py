import time, sys
from random import randint

points = 0
points_to_win = 4000

play_again = True

number_of_dice = 6

dice_in_round = [0,0,0,0,0,0]
name_of_dice = ['A','B','C','D','E','F']
order_of_dice_round = [' ',' ',' ',' ',' ',' ']




class dice_round():
    def __init__(self, id, A, B, C, D, E, F):
        self.id = id
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.dice = [A,B,C,D,E,F]

    # returns number of none zero dice
    def num_values(self):
        num = 0
        for i in range(6):
            if self.dice[i] != 0:
                num += 1
        print(num)    
        return num

    def returndice(self):
        return self.dice

def roll ():
    return randint(1,6)

def new_round_rolls():
    for i in num

def count_points():
    pass

def play_round():
    global number_of_dice
    global name_of_dice
    global dice_in_round

    for i in range(number_of_dice):
        dice_in_round[i] = roll()
        print("Dice " + str(name_of_dice[i]) + ": " + str(dice_in_round[i]))
    
    input_string = input("Enter order of dice to keep seperated by spaces. Ex. A D E F \n")
    input_string = input_string.upper()
    order_of_dice_round = input_string.split()

    validate_set_of_dice(order_of_dice_round, number_of_dice)

def validate_set_of_dice(order_of_dice_round, number_of_dice):
    flag_unique = 0
    flag_num_of_entries = 0
    flag_acceptable_input = 0

    # round_restart = 0

    name_of_dice_VALIDATION = ['AA','BB','CC','DD','EE','FF']

    #check if correct number of dice
    if number_of_dice == len(order_of_dice_round):
        flag_num_of_entries = 1
    else:
        print("Make sure you entered the correct amount of dice")
        
    #check if each dice is used only once:  unique entries - total entries 
    flag_unique = ( len(set(order_of_dice_round)) == len(order_of_dice_round) )

    if(flag_unique): 
        print ("List contains all unique elements") 
    else :  
        print ("List contains does not contains all unique elements")

    ##validating user input##
    for i in range(len(order_of_dice_round)):
        if (order_of_dice_round[i] == 'A') or (order_of_dice_round[i] == 'B') or (order_of_dice_round[i] == 'C') or (order_of_dice_round[i] == 'D') or (order_of_dice_round[i] == 'E') or (order_of_dice_round[i] == 'F'):
            name_of_dice_VALIDATION[i] = order_of_dice_round[i]
            flag_acceptable_input = 1
        else:
            print("Make sure all your dices are A-F")
            flag_acceptable_input = 0
            return
    
    if flag_unique and flag_num_of_entries and flag_acceptable_input:
        pass
    else :
        pass


###############Checking for point values (from highest to lowest)####################
# if order_of_dice_round


while play_again:
    # play_round()
    dice1 = dice_round(1,0,0,0,1,2,3)
    dice1.num_values()
    dice1.returndice()
    print(dice1.returndice())
    #print(dice_in_round)
    play_again = False