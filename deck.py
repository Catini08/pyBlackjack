import subprocess

suits = ["♠", "♡", "♦", "♣"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.string = f"{number} {suit}"

class deck:
    def __init__(self):
        self.collection = {}

        counter = 0 # helper variable that allows card attributes to be named from self.card1 to self.card52

        for s in suits:
            for n in numbers:
                attr_name = f"card{counter}"
                newcard = card(s, n)
                self.collection[attr_name] = newcard
                counter += 1
    
deck1 = deck()

for i in range(52):
    print(deck1.collection[f"card{i}"].string)

        
    