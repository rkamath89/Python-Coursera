# implementation of card game - Memory

import simplegui
import random

turns=0;
list1 = range(8);
list2 = range(8);
combinedList = list1+list2;
exposedIndex = range(16);
for i in range(16):
    exposedIndex[i] = 0;
random.shuffle(combinedList);
clicked = -1;
drawCards = True;
state = 0; #0 means 1 card, 1 means 2 cards, 2 means reset
card1Value=-1;
card2Value=-1;
# helper function to initialize globals
def new_game():
    global turns,state,card2Value,card1Value,exposedIndex,combinedList;
    turns = 0;
    state = 0;
    card1Value = card2Value = -1;
    for i in range(16):
        exposedIndex[i]=0;
    label.set_text("Turn = "+str(turns));
    random.shuffle(combinedList);

     
# define event handlers
def mouseclick(pos):
    global turns,state,card1Value,card2Value,exposedIndex;
    clicked = pos[0]/50;
    if(exposedIndex[clicked] != 1 and exposedIndex[clicked] != 2): 
        if(state==2):
            state =0;
            
            if(card1Value == card2Value and card1Value != -1 and card2Value != -1):
                for i in range(16):
                    if(exposedIndex[i] == 1):
                        exposedIndex[i] = 2;
            else:
                for i in range(16):
                    if(exposedIndex[i] == 1):
                        exposedIndex[i] = 0;
            
            card1Value =card2Value = -1;            
            
            
        exposedIndex[clicked] = 1;    
        if(state==0):
            turns = turns+1;
            state=1;
            card1Value=combinedList[clicked];
        elif(state==1):
            state=2;
            
            card2Value=combinedList[clicked];
        #print turns;
        label.set_text("Turn = "+str(turns));
    
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global drawCards;
    for i in range(16):
        if(exposedIndex[i] == 0):
            canvas.draw_polygon([( i*50, 0), ((i+1)*50, 0), ((i+1)*50, 100),((i)*50,100)], 3, 'Blue', 'Green')
        if(exposedIndex[i] == 1 or exposedIndex[i] == 2):
            #print combinedList[i],i;
            canvas.draw_text(str(combinedList[i]), (i*50+5,90), 90, "RED");
            


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turn = "+str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric