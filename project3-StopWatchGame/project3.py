# template for "Stopwatch: The Game"
import simplegui;

# define global variables
tenSeconds = 0;
A =0;
B = 0;
C = 0;
D =0;
timerRunning=0;
winCount=0;
lossCount=0;
score = str(winCount)+"/"+str(lossCount);
formatedString =str(A)+":"+str(B)+str(C)+":"+str(D);
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A,B,C,D,formatedString;
    D = t%10;
    C = ((t%100)-D)//10;
    temp = (t-(t%100))//100;
    B=temp%6;
    A=temp//6;
    formatedString=str(A)+":"+str(B)+str(C)+":"+str(D);
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startHandler():
    global timerRunning;
    timerRunning = 1;
    timer.start();
def stopHandler():
    global winCount,lossCount,score,timerRunning;
   
    timer.stop();
    if(timerRunning == 1):
        if( D == 0):
            winCount = winCount+1;
        else:
            lossCount = lossCount+1;
    
    score = str(winCount)+"/"+str(lossCount);
    timerRunning = 0;
    
def resetHandler():
    global A,B,C,D,tenSeconds,formatedString,score,winCount,lossCount;
    tenSeconds = 0;
    A =0;
    B = 0;
    C = 0;
    D =0;
    lossCount = 0;
    winCount =0;
    formatedString=str(A)+":"+str(B)+str(C)+":"+str(D);
    score = str(winCount)+"/"+str(lossCount);
    
def timerHandler():
    global tenSeconds;
    tenSeconds = tenSeconds + 1;
    #print tenSeconds;
    format(tenSeconds);


# define draw handler
def draw(canvas):
    canvas.draw_text(str(formatedString),[130,150],34,"RED");
    canvas.draw_text(str(score),[200,200],20,"GREEN");

    
# create frame
frame = simplegui.create_frame("Stop Watch",300,300);
frame.set_draw_handler(draw);
# register event handlers
frame.add_button("Start",startHandler,100);
frame.add_button("Stop",stopHandler,100);
frame.add_button("Reset",resetHandler,100);
timer = simplegui.create_timer(100,timerHandler);

# start frame
frame.start();

#print format(0)
#print format(7)
#print format(17)
#print format(60)
#print format(63)
#print format(214)
#print format(599)
#print format(600)
#print format(602)
#print format(667)
#print format(1325)
#print format(4567)
#print format(5999)
###################################################
# Output from test

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9
