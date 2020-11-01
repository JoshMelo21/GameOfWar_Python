import random
import pdb
from Deck import Deck
suits= ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

class Player:
    def __init__(self, name):
        self.name =  name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return "Player: " + self.name + " has " + len(self.all_cards) + " cards."


# Create Players
p1 = Player("One")
p2 = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    p1.add_cards(new_deck.deal_one())
    p2.add_cards(new_deck.deal_one())

#Game Loop
game = True
counter = 0
while game:
    counter += 1
    print("Currently on round {}".format(counter))
    print("P1 cards {}".format(len(p1.all_cards)))
    print("P2 cards {}".format(len(p2.all_cards)))
    if len(p1.all_cards)==0:
        print("Player 2 has won")
        game =False
        break
    if len(p2.all_cards)==0:
        print("Player 1 has won")
        game =False
        break
    p1_face_up =[]
    p2_face_up =[]
    p1_face_up.append(p1.remove_one())
    p2_face_up.append(p2.remove_one())

    at_war = True

    while at_war:

        if p1_face_up[-1].value > p2_face_up[-1].value:
            p1.add_cards(p1_face_up)
            p1.add_cards(p2_face_up)
            at_war = False
        elif p2_face_up[-1].value > p1_face_up[-1].value:
            p2.add_cards(p1_face_up)
            p2.add_cards(p2_face_up)
            at_war = False
        else:
            print("War")
        
            if len(p1.all_cards) <3:
                print("Player 1 does not have enough cards for war. Player 2 wins.")
                game= False
                break
            elif len(p2.all_cards) <3:
                print("Player 2 does not have enough cards for war. Player 1 wins.")
                game =False
                break
            else:
                for num in range(3):
                    p1_face_up.append(p1.remove_one())
                    p2_face_up.append(p2.remove_one())
        