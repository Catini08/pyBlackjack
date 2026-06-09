import subprocess
import os
import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def clear():
    subprocess.run(
        ['cls' if os.name == 'nt' else 'clear']
    )

suits = ["♠", "♡", "♦", "♣"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

val_counter = 0 # dynamic value for each card
values = {f"{numbers[c]}": c for c in range(len(numbers))}


class card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.value = values[number]
        if self.suit == "♡" or self.suit == "♦":
            self.stringstyle = Back.WHITE + Fore.RED
        else:
            self.stringstyle = Back.WHITE + Fore.BLACK
        self.string = f"{self.stringstyle}{Style.BRIGHT}{number} {suit}{Style.NORMAL}"
    def glyph_show(self): # card glyph displayer
        if self.suit == "♡" or self.suit == "♦":
            style = Back.WHITE + Fore.RED
        else:
            style = Back.WHITE + Fore.BLACK
        n_top = self.number.ljust(2)
        n_bot = self.number.rjust(2)
        s = self.suit

        if self.value == 0:  # Ace (1 center symbol)
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style}         ")
            print(f"{style}    {s}    ")
            print(f"{style}         ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 1:  # 2 (Top and Bottom)
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style}    {s}    ")
            print(f"{style}         ")
            print(f"{style}    {s}    ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 2:  # 3 (Top, Middle, Bottom)
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style}    {s}    ")
            print(f"{style}    {s}    ")
            print(f"{style}    {s}    ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 3:  # 4 (Four corners)
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style}  {s}   {s}  ")
            print(f"{style}         ")
            print(f"{style}  {s}   {s}  ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 4:  # 5 (Four corners + Middle)
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style}  {s}   {s}  ")
            print(f"{style}    {s}    ")
            print(f"{style}  {s}   {s}  ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 5:  # 6 (Two columns of three)
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style}  {s}   {s}  ")
            print(f"{style}  {s}   {s}  ")
            print(f"{style}  {s}   {s}  ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 6:  # 7 (Two columns of three + One upper middle)
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style}  {s}   {s}  ")
            print(f"{style}  {s} {s} {s}  ")
            print(f"{style}  {s}   {s}  ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 7:  # 8 
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style} {s}  {s}  {s} ")
            print(f"{style}    {s}    ")
            print(f"{style} {s}  {s}  {s} ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 8:  # 9 (Three columns of three)
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style} {s}  {s}  {s} ")
            print(f"{style} {s}  {s}  {s} ")
            print(f"{style} {s}  {s}  {s} ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 9:  # 10 
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style} {s}  {s}  {s} ")
            print(f"{style}  {s}   {s}  ")
            print(f"{style} {s}  {s}  {s} ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 10:  # Jack
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style}   {s} {s}   ")
            print(f"{style}    {s}    ")
            print(f"{style}   {s} {s}   ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 11:  # Queen
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style}   {s}{s}{s}   ")
            print(f"{style}   {s} {s}   ")
            print(f"{style}   {s}{s}{s}   ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

        elif self.value == 12:  # King
            print(f"{style}{n_top}       ")
            print(f"{style}         ")
            print(f"{style}  {s} {s} {s}  ")
            print(f"{style}   {s}{s}{s}   ")
            print(f"{style}  {s} {s} {s}  ")
            print(f"{style}         ")
            print(f"{style}       {n_bot}")

class deck:
    def __init__(self):
        self.collection = {}
        self.quantity = len(suits) * len(numbers) # dynamically counts the cards
        counter = 0 # helper variable to populate the collection set
        for s in suits: # dynamically creates the card collection
            for n in numbers:
                self.collection[f"card{counter}"] = card(s, n)
                counter += 1
        self.order = [self.collection[f"card{c}"] for c in range(self.quantity)] # set that actually stores the order of the cards

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
        print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nShuffling")
        time.sleep(0.15)
        clear()
        print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nShuffling.")
        time.sleep(0.15)
        clear()
        print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nShuffling..")
        time.sleep(0.15)
        clear()
        print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nShuffling...")
        time.sleep(0.15)

    clear()
    print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nDeck shuffled!")
    time.sleep(1)

def pick_anim(): # pick animation
    for _ in range(3):
        clear()
        print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nPicking")
        time.sleep(0.15)
        clear()
        print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nPicking.")
        time.sleep(0.15)
        clear()
        print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nPicking..")
        time.sleep(0.15)
        clear()
        print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nPicking...")
        time.sleep(0.15)
    clear()

menu_state = 0
expl_menu_state = 0
deck_is_created = False

while True:
    if menu_state == 0: # main menu
        if deck_is_created == False:
            clear()
            print(
                f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Main menu  {Style.RESET_ALL}\n"
                f"\n"
                f" {Fore.CYAN}[1]{Fore.WHITE} Create deck\n\n"
                f" {Fore.CYAN}[2]{Fore.WHITE} Play Blackjack\n\n"
                f" {Fore.CYAN}[3]{Fore.WHITE} End session\n\n"
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
                print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Main menu  {Style.RESET_ALL}\nDeck created!")
                time.sleep(0.8)
                continue
            else:
                menu_state_first = menu_state
                continue
        else:
            clear()
            print(
                f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Main menu  {Style.RESET_ALL}\n"
                f"\n"
                f" {Fore.CYAN}[1]{Fore.WHITE} Explore deck\n\n"
                f" {Fore.CYAN}[2]{Fore.WHITE} Play Blackjack\n\n"
                f" {Fore.CYAN}[3]{Fore.WHITE} End session\n\n"
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
                f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\n"
                f"\n"
                f" {Fore.CYAN}[1]{Fore.WHITE} Shuffle deck\n\n"
                f" {Fore.CYAN}[2]{Fore.WHITE} Pick first card\n\n"
                f" {Fore.CYAN}[3]{Fore.WHITE} Pick any card\n\n"
                f" {Fore.CYAN}[4]{Fore.WHITE} Pick specific card\n\n"
                f" {Fore.CYAN}[5]{Fore.WHITE} Exit exploration\n\n"
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
            first_card = deck1.pick_first()
            print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nThe first card is {first_card.string}!\n")
            first_card.glyph_show()

            enter = input("\n\n[ENTER] = Return")
            expl_menu_state = 0
            continue
        elif expl_menu_state == 3: # pick any card
            clear()
            pick_anim()
            any_card = deck1.pick_any()
            print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nYou picked {any_card.string}!\n")
            any_card.glyph_show()

            enter = input("\n[ENTER] = Return")
            expl_menu_state = 0
            continue
        elif expl_menu_state == 4: # pick specific card on given position
            clear()
            print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nChoose a position from 0 to {deck1.quantity}.")
            print(f"{Fore.LIGHTBLACK_EX}-> In this case, 0 is the card on top and {deck1.quantity} is the card in the bottom.")
            

            pick_position = int(input("\nDesired position: "))
            picked_in_pos = deck1.pick_in_position(pick_position)
            pick_anim()
            clear()
            print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nCard in position {pick_position} is {picked_in_pos.string}!\n")
            picked_in_pos.glyph_show()

            enter = input("\n[ENTER] = Return")
            expl_menu_state = 0
            continue
        elif expl_menu_state == 5:
            clear()
            expl_menu_state = 0
            menu_state = 0
            continue
        elif expl_menu_state == 10: # invalid character
            clear()
            print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nInvalid input.")
            expl_menu_state = 0
            enter = input("\n\n[ENTER] = Try again")
            continue
        else: # invalid integer state
            clear()
            print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Exploring deck {Style.RESET_ALL}\nInvalid input.")
            expl_menu_state = 0
            enter = input("\n\n[ENTER] = Try again")
            continue
    elif menu_state == 10: # invalid input state
        clear()
        print(f"{Back.WHITE}{Fore.RED}● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards{Style.NORMAL}{Fore.BLACK} - Main menu {Style.RESET_ALL}\nInvalid input.")
        menu_state = 0
        enter = input("\n\n[ENTER] = Try again")
        continue
            