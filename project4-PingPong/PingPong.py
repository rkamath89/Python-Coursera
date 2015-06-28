# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [ WIDTH/2,HEIGHT/2 ];
ball_vel = [ WIDTH/2,HEIGHT/2 ];
score1=0;
score2=0;
paddle1_pos = [0,HEIGHT/2];
paddle2_pos = [WIDTH,HEIGHT/2];
paddle1_vel = 0;
paddle2_vel = 0;
paddleTopTemp=0;
paddleBottomTemp=0;
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos[0] = WIDTH/2;
    ball_pos[1] = HEIGHT/2;
    ball_vel[0] = random.randrange(120, 240)/60.0;
    ball_vel[1] = random.randrange(60, 180)/60.0;
    if(direction == "left"):
        ball_vel[0] = -ball_vel[0];
        ball_vel[1] = -ball_vel[1];
    if(direction == "right"):
        ball_vel[0] = ball_vel[0];
        ball_vel[1] = -ball_vel[1];

        
#RESE
def reset():
    global score1,score2,paddle1_pos,paddle2_pos;
    score1 = score2 = 0;
    paddle1_pos = [0,HEIGHT/2];
    paddle2_pos = [WIDTH,HEIGHT/2];
    new_game();
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    direction = random.randrange(0,2);
    if(direction == 0):
        spawn_ball("right");
    else:
        spawn_ball("left");

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddleTopTemp,paddleBottomTemp;
    score1Str = str(score1);
    score2Str = str(score2);
        
    #Paddle Update
    if((paddle1_pos[1]-40+paddle1_vel >= 0) and (paddle1_pos[1]+40+paddle1_vel <= HEIGHT) ):
        paddle1_pos[1] = paddle1_pos[1]+paddle1_vel;
    if((paddle2_pos[1]-40+paddle2_vel >= 0) and (paddle2_pos[1]+40+paddle2_vel <= HEIGHT) ):
        paddle2_pos[1] = paddle2_pos[1]+paddle2_vel;
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([paddle1_pos[0],paddle1_pos[1]-40],[paddle1_pos[0],paddle1_pos[1]+40],13, "White");
    canvas.draw_line([paddle2_pos[0],paddle2_pos[1]-40],[paddle2_pos[0],paddle2_pos[1]+40],13, "White");
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(score1Str,(130,120),42,"RED");
    canvas.draw_text(score2Str,(430,120),42,"RED");
    
        
    # update ball   
    if(ball_pos[1]-BALL_RADIUS <= 0 or ball_pos[1]+BALL_RADIUS >= HEIGHT ):
        ball_vel[1] = -ball_vel[1];
    if(ball_pos[0]-BALL_RADIUS <= PAD_WIDTH):
        if (ball_pos[1] < (paddle1_pos[1] - HALF_PAD_HEIGHT)) or (ball_pos[1] > (paddle1_pos[1] + HALF_PAD_HEIGHT)):
            score2 += 1
            spawn_ball("right");
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
    if(ball_pos[0]+BALL_RADIUS >= WIDTH-PAD_WIDTH):
        if (ball_pos[1] < (paddle2_pos[1] - HALF_PAD_HEIGHT)) or (ball_pos[1] > (paddle2_pos[1] + HALF_PAD_HEIGHT)):
            score1 += 1
            spawn_ball("left");
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
    
    ball_pos[0]  = ball_pos[0]+ball_vel[0];
    ball_pos[1]  = ball_pos[1]+ball_vel[1];

    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,10,"WHITE","WHITE");
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel;
    if(simplegui.KEY_MAP['w'] == key ):
        paddle1_vel = paddle1_vel-4;
    elif(simplegui.KEY_MAP['s'] == key ):
        paddle1_vel = paddle1_vel+4;
    
    if(simplegui.KEY_MAP['up'] == key ):
        paddle2_vel = paddle2_vel-4;
    elif(simplegui.KEY_MAP['down'] == key ):
        paddle2_vel = paddle2_vel+4;
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(simplegui.KEY_MAP['up'] == key ):
        paddle2_vel = 0;
    elif(simplegui.KEY_MAP['down'] == key ):
        paddle2_vel = 0;
    if(simplegui.KEY_MAP['w'] == key ):
        paddle1_vel = 0;
    elif(simplegui.KEY_MAP['s'] == key ):
        paddle1_vel = 0;


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("RESET",reset);
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
