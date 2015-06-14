# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random;

# Global Variable
secret_number=0;
isFirstTime = 0;
# 0 means 0-100 1 means 0-1000
range_val = 0;
numberOfTries=7;
isReset =0;
# helper function to start and restart the game
def new_game():
    global secret_number;
    global numberOfTries;
    global isFirstTime;
    global isReset;
    if(range_val == 0):
        if(isFirstTime == 0 or isReset == 1):
            isReset = 0;
            isFirstTime =1;
            print "";
            print "New game. Range is from 0 to 100";
            print "Number of remaining guesses is 7"
        secret_number = random.randrange(0,100);
        numberOfTries = 7;
    else:
        if(isReset == 1):
            isReset = 0;
            print "";
            print "New game. Range is from 0 to 1000";
            print "Number of remaining guesses is 10";
        secret_number = random.randrange(0,1000);
        numberOfTries = 10;
            


# define event handlers for control panel
def range100():
    global range_val;
    range_val = 0;
    print " ";
    print "New game. Range is from 0 to 100";
    print "Number of remaining guesses is 7"
    new_game();

def range1000():
    global range_val;
    range_val = 1;
    print " ";
    print "New game. Range is from 0 to 1000";
    print "Number of remaining guesses is 10"
    new_game();
    
def input_guess(guess):
    global numberOfTries,isReset;
    numberOfTries=numberOfTries-1;
    userGuess = int(guess);
    
    print "";    
    if(numberOfTries > 0):
        print "Guess was "+guess;
        print "Number of remaining guesses is "+str(numberOfTries);
        if(userGuess < secret_number):
            print "Lower";
        elif(userGuess > secret_number):
            print "Higher";
        else:
            print "Corect";
            isReset =1;
            new_game();
    else:
        print "You ran out of guesses.  The number was "+str(secret_number);
        isReset =1;
        new_game();
            
        
# create frame
f = simplegui.create_frame("Guess the Number",300,300);


# register event handlers for control elements and start frame
f.add_button("Range: 0 - 100",range100,200);
f.add_button("Range: 0 - 1000",range1000,200);
f.add_input("Enter a Guess: ",input_guess,200);
f.start();
# call new_game 
new_game();


# always remember to check your completed program against the grading rubric
