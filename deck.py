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
        suits = ["♠", "♡", "♦", "♣"]
        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        counter = 0 # helper variable that allows card attributes to be named
        for s in suits: # dynamically creates the card collection
            for n in numbers:
                attr_name = f"card{counter}"
                newcard = card(s, n)
                self.collection[attr_name] = newcard
                counter += 1
        self.order = ["" for i in range(counter)]
        for c in range(counter): # inserts all cards in a set, representing the card order, that can later be suffled
            self.order[c] = self.collection[f"card{c}"].string
    def shuffle(self):
        random.shuffle(self.order)
    def pick_first(self):
        return self.order[0]
    def pick_any(self):
        return self.order[random.randint(0, 52)]
    

deck1 = deck()

for i in range(52):
    print(deck1.collection[f"card{i}"].string)

print(f"\n")
deck1.shuffle()
print(deck1.order)
print(deck1.pick_first())
print(deck1.pick_any())