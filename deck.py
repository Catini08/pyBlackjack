import subprocess
import os
import random
import time

def clear():
    subprocess.run(
        ['cls' if os.name == 'nt' else 'clear']
    )

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
    def pick_in_position(self, position):
        return self.order[position]

def shuffle_anim():# shuffle animation
    for _ in range(3):
        clear()
        print("Shuffling")
        time.sleep(0.2)
        clear()
        print("Shuffling.")
        time.sleep(0.2)
        clear()
        print("Shuffling..")
        time.sleep(0.2)
        clear()
        print("Shuffling...")
        time.sleep(0.2)

    clear()
    print("Deck shuffled!")
    time.sleep(1)

def pick_anim(): # pick animation
    for _ in range(3):
        clear()
        print("Picking")
        time.sleep(0.2)
        clear()
        print("Picking.")
        time.sleep(0.2)
        clear()
        print("Picking..")
        time.sleep(0.2)
        clear()
        print("Picking...")
        time.sleep(0.2)
    clear()

menu_state = 0
expl_menu_state = 0
deck_is_created = False

while True:
    if menu_state == 0: # main menu
        if deck_is_created == False:
            clear()
            print(
                "------------INTERACTIVE DECK OF CARDS------------" \
                "\n" \
                "-------------------Main menu---------------------" \
                "\n\n\n" \
                "[1] - Create deck\n\n[2] - Play Blackjack\n\n[3] - End session" \
                "\n\n"
                )
            
            burnervar = input("Desired option: ") # protects code from bad user input
            if burnervar.isdigit():
                menu_state_first = int(burnervar)
            else:
                menu_state = 10
                continue

            if menu_state_first == 1: # creating deck
                clear()
                deck_is_created = True
                deck1 = deck()
                print("Deck created!")
                time.sleep(0.8)
                continue
            else:
                menu_state_first = menu_state
                continue
        else:
            clear()
            print(
                "------------INTERACTIVE DECK OF CARDS------------" \
                "\n" \
                "-------------------Main menu---------------------" \
                "\n\n\n" \
                "[1] - Explore deck\n\n[2] - Play Blackjack\n\n[3] - End session" \
                "\n\n"
                )
            
            burnervar = input("Desired option: ")
            if burnervar.isdigit():
                menu_state = int(burnervar)
                continue
            else:
                menu_state = 10
                burnervar = 0
                continue
    if menu_state == 1: # explore deck menu
        if expl_menu_state == 0:
            clear()
            print(
                    "------------INTERACTIVE DECK OF CARDS------------" \
                    "\n" \
                    "-----------------Exploring deck------------------" \
                    "\n\n\n" \
                    "[1] - Shuffle deck\n\n[2] - Pick first card\n\n[3] - Pick any card\n\n[4] - Pick specific card\n\n[5] - Exit exploration" \
                    "\n\n"
                    )
            burnervar = input("Desired option: ")
            if burnervar.isdigit():
                expl_menu_state = int(burnervar)
                continue
            else:
                burnervar = 0
                expl_menu_state = 10
                continue
        elif expl_menu_state == 1: # shuffle deck
            shuffle_anim()
            deck1.shuffle()
            clear()
            expl_menu_state = 0
            continue
        elif expl_menu_state == 2: # pick first
            clear()
            pick_anim()
            clear()
            print(f"The first card is {deck1.pick_first()}!")

            enter = input("\n\n[ENTER] = Return")
            expl_menu_state = 0
            continue
        elif expl_menu_state == 3: # pick any card
            clear()
            pick_anim()
            print(f"You picked {deck1.pick_any()}!")
            enter = input("\n\n[ENTER] = Return")
            expl_menu_state = 0
            continue
        elif expl_menu_state == 4: # pick specific card on given position
            clear()
            print(f"Choose a position from 0 to {deck1.quantity}.\n-> In this case, 0 is the card on top and {deck1.quantity} is the card in the bottom.")
            pick_position = int(input("\nDesired position: "))
            picked_in_pos = deck1.pick_in_position(pick_position)
            pick_anim()
            clear()
            print(f"Card in position {pick_position} is {picked_in_pos}!")

            enter = input("\n\n[ENTER] = Return")
            expl_menu_state = 0
            continue
        elif expl_menu_state == 5:
            clear()
            expl_menu_state = 0
            menu_state = 0
            break
        elif expl_menu_state == 10: # invalid character
            clear()
            print("Invalid input.")
            expl_menu_state = 0
            enter = input("\n\n[ENTER] = Try again")
            continue
        else: # invalid integer state
            clear()
            print("Invalid input.")
            expl_menu_state = 0
            enter = input("\n\n[ENTER] = Try again")
            continue
    elif menu_state == 10: # invalid input state
        clear()
        print("Invalid input.")
        menu_state = 0
        enter = input("\n\n[ENTER] = Try again")
        continue
            