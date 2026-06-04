import subprocess
import random

class card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.string = f"{number} {suit}"

class deck:
    def __init__(self):
        self.collection = {}
        self.order = {}
        suits = ["♠", "♡", "♦", "♣"]
        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        counter = 0 # helper variable that allows card attributes to be named
        for s in suits: # dynamically creates the card collection
            for n in numbers:
                attr_name = f"card{counter}"
                newcard = card(s, n)
                self.collection[attr_name] = newcard
                counter += 1
        for c in range(counter): # associates all cards to a number, representing its spot in the deck.
            self.order[self.collection[f"card{c}"].string] = c
    def shuffle():
        spots = [i for i in range(52)]


deck1 = deck()

for i in range(52):
    print(deck1.collection[f"card{i}"].string)
print(deck1.order)
        
spots = [i for i in range(52)]
print(spots[1])