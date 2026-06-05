import subprocess
import random

def clear():
    subprocess.run(
        ['cls' if os.name == 'nt' else 'clear']
    )

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
        self.quantity = len(suits) * len(numbers) # dynamically counts the cards
        counter = 0 # helper variable to populate the collection set
        for s in suits: # dynamically creates the card collection
            for n in numbers:
                self.collection[f"card{counter}"] = card(s, n)
                counter += 1
        self.order = [self.collection[f"card{c}"].string for c in range(self.quantity)] # set that actually stores the order of the cards

    def shuffle(self):
        random.shuffle(self.order)
    def pick_first(self):
        return self.order[0]
    def pick_any(self):
        return self.order[random.randint(0, self.quantity)] # 
    

deck1 = deck()

for i in range(deck1.quantity):
    print(deck1.collection[f"card{i}"].string)

print(f"\n")
deck1.shuffle()
print(deck1.order)
print(deck1.pick_first())
print(deck1.pick_any())