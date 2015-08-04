# Mini-project #6 - Blackjack
#Can Test the Code : http://www.codeskulptor.org/#user40_xZ3jlbTHlI_15.py
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0;
win=0;
lose =0;
playersValue =0;
dealersValue =0;
playerMessage = "Hit or Stand ?";
dealerMessage ="";
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.listOfCards = list();

    def __str__(self):
        ans="Hand contains ";
        for i in range(len(self.listOfCards)):
            ans += " "+str(self.listOfCards[i].suit)+str(self.listOfCards[i].rank);
        return ans;
            

    def add_card(self, card):
        self.listOfCards.append(card);

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        doesAceExist= False;
        global in_play;
        for i in range(len(self.listOfCards)):
            if("A" == self.listOfCards[i].rank):
                doesAceExist = True;
                #print doesAceExist;
                break;
        handValue = 0;
        for i in range(len(self.listOfCards)):
            tempCard = self.listOfCards[i];
            valueOfCard = VALUES.get(tempCard.rank);
            handValue +=valueOfCard;
        if(doesAceExist == False):
            return handValue;
        if(doesAceExist == True):
            if(handValue+10 <= 21):
                return handValue+10;
            else:
                return handValue;
    
    def draw(self, canvas, pos,player):
        for i in range(len(self.listOfCards)):
            tempCard = self.listOfCards[i];
            newPos = pos;
            newPos[0] = i*72;
            newPos[1] = pos[1];
            if(player == "D" and in_play):
                if(i==0):
                    tempCard.draw(canvas, newPos);
                if( i == 1):
                    card_loc = (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1]);
                    canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [newPos[0] + CARD_BACK_CENTER[0], newPos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
                    break;
            else:
                tempCard.draw(canvas, newPos);
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cardDeck = list();
        for s in range(len(SUITS)):
            for r in range(len(RANKS)):
                newCard = Card(SUITS[s],RANKS[r]);
                self.cardDeck.append(newCard);

    def shuffle(self):
        random.shuffle(self.cardDeck);
        
    def deal_card(self):
        value = random.randrange(0,len(self.cardDeck));
        card = self.cardDeck.pop(value);
        return card;
    
    def __str__(self):
        result="Deck contains "
        for i in range(len(self.cardDeck)):
            card = self.cardDeck[i];
            result +=" "+str(card.suit)+str(card.rank);
        return result;
            
newDeck = Deck();
playerHand = Hand();
dealerHand = Hand();
#define event handlers for buttons
def deal():
    
    global playerMessage,dealerMessage,playersValue,newDeck,outcome,newDeck,in_play,win,lose,playerHand,dealerHand;
    if(in_play):
        lose = lose+1;
        dealerMessage = "Player Loses, Dealer Wins !!!";
    playerMessage = "Hit or Stand ?";
    if(in_play == False):
        dealerMessage ="";
    in_play = True
    newDeck = Deck();
    newDeck.shuffle();
    playerHand = Hand();
    dealerHand = Hand();
    # Get 2 Cards For Dealer
    card1 = newDeck.deal_card();
    dealerHand.add_card(card1);
    card2 = newDeck.deal_card();
    dealerHand.add_card(card2);
    print "Dealer :: "+str(card1)+","+str(card2);
    
    # Get 2 Cards For Player
    card1 = newDeck.deal_card();
    playerHand.add_card(card1);
    card2 = newDeck.deal_card();
    playerHand.add_card(card2);
    playersValue = playerHand.get_value();
    print "Player :: "+str(card1)+","+str(card2);
    if(playersValue == 21):
            dealerMessage = "Player win's !!!";
            playerMessage = "New Deal ?";
            win=win+1;
            in_play = False;
            return;
    

def hit(): 
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global playerHand,in_play,win,lose,newDeck,playerMessage,dealerMessage;
    if(in_play == True):
        dealerMessage="";
        playerMessage= "Hit or Stand ?";
        newCard = newDeck.deal_card();
        print "Card Delt :"+str(newCard);
        playerHand.add_card(newCard);
        playersValue = playerHand.get_value();
        print "Players Hand Value :"+str(playersValue);
        if(playersValue == 21):
            dealerMessage = "Player win's !!!";
            playerMessage = "New Deal ?";
            win=win+1;
            in_play= False;
            return;
        if(playersValue > 21):
            dealerMessage = "Busted , Player Loses";
            playerMessage=  "New Deal ?";
            in_play = False;
            lose = lose+1;
        
        
    
       
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global playerHand,win,lose,dealerHand,in_play,newDeck,playerMessage,dealerMessage;
    if(in_play == True):
        dealerMessage="";
        playersValue = playerHand.get_value();
        if(playersValue > 21):
            dealerMessage = "Busted , Player Loses";
            playerMessage=  "New Deal ?";
            in_play=False;
            lose=lose+1;
            return;
        dealerValue = dealerHand.get_value();
        while(dealerValue <= 17 ):
            newCard = newDeck.deal_card();
            print "Card Delt for Dealer :"+str(newCard);
            dealerHand.add_card(newCard);
            dealerValue = dealerHand.get_value();
            print "Dealer Hand Value :"+str(dealerValue);

        if(dealerValue > 21):
            dealerMessage = "Player win's !!!";
            playerMessage = "New Deal ?";
            win=win+1;
            in_play=False;
            return;
    
        if(dealerValue <=21 and playersValue <=21):
            if(dealerValue == playersValue):
                dealerMessage = "Player Loses, Dealer Wins !!!";
                playerMessage = "New Deal ?";
                lose=lose+1
                in_play=False;
            elif(dealerValue > playersValue):
                dealerMessage = "Player Loses, Dealer Wins !!!";
                playerMessage = "New Deal ?";
                lose=lose+1;
                in_play=False;

            else:
                dealerMessage = "Player win's !!!";
                playerMessage = "New Deal ?";
                win=win+1;
                in_play=False;
    in_play=False;
        
    

# draw handler    
def draw(canvas):
    global playerHand,dealerHand,win,lose,playerMessage,dealerMessage,in_play;
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BlackJack",(250,25),32,"BLACK");
    canvas.draw_text("Dealer",(0,45),32,"BLACK");
    canvas.draw_text("Player",(0,325),32,"BLACK");
    canvas.draw_text("Score",(450,45),32,"BLUE");
    canvas.draw_text("Wins :"+str(win),(450,65),22,"BLACK");
    canvas.draw_text("Lose :"+str(lose),(450,85),22,"BLACK");
    canvas.draw_text("Total :"+str(win-lose),(450,115),22,"BLACK");
    canvas.draw_text(playerMessage,(150,325),22,"WHITE");
    canvas.draw_text(dealerMessage,(100,55),22,"WHITE");
    playerHand.draw(canvas,[0,350],"P");
    dealerHand.draw(canvas,[0,100],"D");
    val = playerHand.get_value();
    canvas.draw_text("Player Hand Value :"+str(val),(0,500),22,"BLACK");


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric