# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import math;
import random;

def name_to_number(name):
    if name == "rock":
        return 0;
    elif name == "Spock":
        return 1;
    elif name == "paper":
        return 2;
    elif name == "lizard":
        return 3;
    elif name == "scissors":
        return 4;
    else: # Default case:
        return -1;


def number_to_name(number):
    if number == 0:
        return "rock";
    elif number == 1:
        return "Spock";
    elif number == 2:
        return "paper";
    elif number == 3:
        return "lizard";
    elif number == 4:
        return "scissors";
    else: # Default case
        return "empty";
    

def rpsls(player_choice): 
    
    print "";

    print "Player chooses "+player_choice;

    playersChoiceNumber = name_to_number(player_choice);

    randomChoice =random.randrange(0,4);

    randomChoiceName = number_to_name(randomChoice);
    
    print "Computer chooses "+randomChoiceName;

    # compute difference of comp_number and player_number modulo five
    difference  = (randomChoice-playersChoiceNumber)%5;
    #print difference;
    # use if/elif/else to determine winner, print winner message
    if(difference == 0):
        print "Player and computer tie!";
    elif(difference <= 2):
         print "Computer wins!";
    else:
        print "Player wins!";
       

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


