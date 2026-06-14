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

def UI_top_bar():
    print(f"{Back.WHITE}{Fore.RED} ● {Fore.YELLOW}● {Fore.GREEN}●  {Style.BRIGHT}{Fore.BLACK}Interactive Deck of Cards                  {Style.NORMAL}{Fore.BLACK}{Style.RESET_ALL}")

def submenu_info(menuname):
    print(f"\n{Back.BLUE} • {Back.WHITE}{Fore.BLACK} {menuname} {Style.RESET_ALL}\n")


suits = ["♠", "♡", "♦", "♣"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# values had to be hardcoded because of glyph_show() and blackjack
values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

class card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.value = values[number]

        self.stringstyle = Back.WHITE + Fore.RED if self.suit == "♡" or self.suit == "♦" else Back.WHITE + Fore.BLACK
        self.string = f"{self.stringstyle}{Style.BRIGHT}{number} {suit}{Style.RESET_ALL}"
    def glyph_lines(self):  # returns the 7 display lines for this card, without printing
        if self.suit == "♡" or self.suit == "♦":
            style = Back.WHITE + Fore.RED
        else:
            style = Back.WHITE + Fore.BLACK
        n_top = self.number.ljust(2)
        n_bot = self.number.rjust(2)
        s = self.suit

        if self.number == "A":  # Ace
            return [
                f"{style}{n_top}       ",
                f"{style}         ",
                f"{style}         ",
                f"{style}    {s}    ",
                f"{style}         ",
                f"{style}         ",
                f"{style}       {n_bot}",
            ]

        elif self.number == "2":
            return [
                f"{style}{n_top}       ",
                f"{style}    {s}    ",
                f"{style}         ",
                f"{style}         ",
                f"{style}         ",
                f"{style}    {s}    ",
                f"{style}       {n_bot}",
            ]

        elif self.number == "3":
            return [
                f"{style}{n_top}       ",
                f"{style}    {s}    ",
                f"{style}         ",
                f"{style}    {s}    ",
                f"{style}         ",
                f"{style}    {s}    ",
                f"{style}       {n_bot}",
            ]

        elif self.number == "4":
            return [
                f"{style}{n_top}       ",
                f"{style}  {s}   {s}  ",
                f"{style}         ",
                f"{style}         ",
                f"{style}         ",
                f"{style}  {s}   {s}  ",
                f"{style}       {n_bot}",
            ]

        elif self.number == "5":
            return [
                f"{style}{n_top}       ",
                f"{style}  {s}   {s}  ",
                f"{style}         ",
                f"{style}    {s}    ",
                f"{style}         ",
                f"{style}  {s}   {s}  ",
                f"{style}       {n_bot}",
            ]

        elif self.number == "6":
            return [
                f"{style}{n_top}       ",
                f"{style}  {s}   {s}  ",
                f"{style}         ",
                f"{style}  {s}   {s}  ",
                f"{style}         ",
                f"{style}  {s}   {s}  ",
                f"{style}       {n_bot}",
            ]

        elif self.number == "7":
            return [
                f"{style}{n_top}       ",
                f"{style}  {s}   {s}  ",
                f"{style}         ",
                f"{style}  {s} {s} {s}  ",
                f"{style}         ",
                f"{style}  {s}   {s}  ",
                f"{style}       {n_bot}",
            ]

        elif self.number == "8":
            return [
                f"{style}{n_top}       ",
                f"{style}  {s}   {s}  ",
                f"{style}    {s}    ",
                f"{style}  {s}   {s}  ",
                f"{style}    {s}    ",
                f"{style}  {s}   {s}  ",
                f"{style}       {n_bot}",
            ]

        elif self.number == "9":
            return [
                f"{style}{n_top}       ",
                f"{style}  {s}   {s}  ",
                f"{style}  {s}   {s}  ",
                f"{style}    {s}    ",
                f"{style}  {s}   {s}  ",
                f"{style}  {s}   {s}  ",
                f"{style}       {n_bot}",
            ]

        elif self.number == "10":
            return [
                f"{style}{n_top}       ",
                f"{style}  {s}   {s}  ",
                f"{style}  {s} {s} {s}  ",
                f"{style}         ",
                f"{style}  {s} {s} {s}  ",
                f"{style}  {s}   {s}  ",
                f"{style}       {n_bot}",
            ]

        else:  # face cards
            emblem = {"J": "♞", "Q": "♛", "K": "♚"}[self.number]
            return [
                f"{style}{n_top}       ",
                f"{style}         ",
                f"{style}    {s}    ",
                f"{style}   {emblem}{emblem}{emblem}   ",
                f"{style}    {s}    ",
                f"{style}         ",
                f"{style}       {n_bot}",
            ]

    def glyph_show(self):  # single-card display, now built on glyph_lines()
        for j in self.glyph_lines():
            print(j)

class deck:
    def __init__(self):
        self.collection = {}
        self.quantity = len(suits) * len(numbers) # dynamically counts the cards
        counter = 0 # helper variable to populate the collection set
        for s in suits: # dynamically creates the card collection
            for n in numbers:
                self.collection[f"card{counter}"] = card(s, n)
                counter += 1
        self.order = [self.collection[f"card{c}"] for c in range(len(self.collection))] # set that actually stores the order of the cards

    def shuffle(self):
        random.shuffle(self.order)
    def pick_first(self):
        return self.order[0]
    def pick_any(self):
        return self.order[random.randint(0, self.quantity)] # 
    def pick_in_position(self, position):
            return self.order[(position - 1)]

def shuffle_anim():# shuffle animation
    for _ in range(3):
        clear()
        UI_top_bar()
        submenu_info("Explore deck menu")
        print("\nShuffling")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Explore deck menu")
        print("\nShuffling.")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Explore deck menu")
        print("\nShuffling..")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Explore deck menu")
        print("\nShuffling...")
        time.sleep(0.15)

    clear()
    UI_top_bar()
    print("\nDeck shuffled!")
    time.sleep(1)

def pick_anim(): # pick animation
    for _ in range(3):
        clear()
        UI_top_bar()
        submenu_info("Explore deck menu")
        print("\nPicking")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Explore deck menu")
        print("\nPicking.")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Explore deck menu")
        print("\nPicking..")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Explore deck menu")
        print("\nPicking...")
        time.sleep(0.15)
    clear()

def mult_cards_display(cardfaces):
    full_rows = ["" for i in range(7)] # populates the full rows list with appendable data
    for i in range(7): # for each line that composes a card
        for c in cardfaces: # for each card in cardfaces
            full_rows[i] += c.glyph_lines()[i] # in the line i, append the line i from card c
            full_rows[i] += f"{Style.RESET_ALL}   "
    for r in range(len(full_rows)):
        print(full_rows[r])

menu_state = 0
expl_menu_state = 0
blkjk_menu_state = 0
deck_is_created = True
deck1 = deck()

while True:
    if menu_state == 0: # main menu
        clear()
        UI_top_bar()
        print(
            f"\n"
            f" {Fore.RED}1{Fore.WHITE} Explore deck\n\n"
            f" {Fore.RED}2{Fore.WHITE} Play Blackjack\n\n"
            f" {Fore.RED}3{Fore.WHITE} End session\n\n"
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
            UI_top_bar()
            submenu_info("Explore deck menu")
            print(
                f" {Fore.RED}1{Fore.WHITE} Shuffle deck\n\n"
                f" {Fore.RED}2{Fore.WHITE} Pick first card\n\n"
                f" {Fore.RED}3{Fore.WHITE} Pick any card\n\n"
                f" {Fore.RED}4{Fore.WHITE} Pick specific card\n\n"
                f" {Fore.RED}5{Fore.WHITE} Exit exploration\n\n"
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
            UI_top_bar()
            submenu_info("Explore deck menu")
            print(f"\nThe first card is {first_card.string}!\n")
            first_card.glyph_show()

            enter = input(f"\n\n{Fore.RED}ENTER{Style.RESET_ALL} = Return")
            expl_menu_state = 0
            continue
        elif expl_menu_state == 3: # pick any card
            clear()
            pick_anim()
            any_card = deck1.pick_any()
            UI_top_bar()
            submenu_info("Explore deck menu")
            print(f"\nYou picked {any_card.string}!\n")
            any_card.glyph_show()

            enter = input(f"\n{Fore.RED}ENTER{Style.RESET_ALL} = Return")
            expl_menu_state = 0
            continue
        elif expl_menu_state == 4: # pick specific card on given position
            clear()
            UI_top_bar()
            submenu_info("Explore deck menu")
            print(f"\nChoose a position from 1 to {deck1.quantity}.")
            print(f"{Fore.LIGHTBLACK_EX}-> In this case, 1 is the card on top and {deck1.quantity} is the card at the bottom.")
            
            burnervar = input("\nDesired position: ")
            if burnervar.isdigit() == False: # protecting script from wrong input
                burnervar = 0
                expl_menu_state = 10
                continue
            else:
                pick_position = int(burnervar)
                if pick_position > deck1.quantity:
                    expl_menu_state = 10
                    continue
                else:
                    picked_in_pos = deck1.pick_in_position(pick_position)
                    pick_anim()
                    clear()
                    UI_top_bar()
                    submenu_info("Explore deck menu")
                    print(f"Card in position {pick_position} is {picked_in_pos.string}!\n")
                    picked_in_pos.glyph_show()

                    enter = input(f"\n{Fore.RED}ENTER{Style.RESET_ALL} = Return")
                    expl_menu_state = 0
                    continue
        elif expl_menu_state == 5:
            clear()
            expl_menu_state = 0
            menu_state = 0
            continue
        elif expl_menu_state == 10: # invalid character
            clear()
            UI_top_bar()
            submenu_info("Explore deck menu")
            print("\nInvalid input.")
            expl_menu_state = 0
            enter = input(f"\n\n{Fore.RED}ENTER{Style.RESET_ALL} = Try again")
            continue
        else: # invalid integer state
            clear()
            UI_top_bar()
            submenu_info("Explore deck menu")
            print("\nInvalid input.")
            expl_menu_state = 0
            enter = input(f"\n\n{Fore.RED}ENTER{Style.RESET_ALL} = Try again")
            continue
    elif menu_state == 2: # BLACKJACK
        balance = 100
        def balance_display():
            print(
                f"{Back.GREEN}{Fore.BLACK} > {Back.WHITE} Your Balance: {Fore.GREEN}${balance} {Style.RESET_ALL}"
            )
        if blkjk_menu_state == 0: # blackjack main menu
            clear()
            UI_top_bar()
            submenu_info("Blackjack")
            print(
                    f"\n"
                    f" {Fore.GREEN}1{Fore.WHITE} Play\n\n"
                    f" {Fore.GREEN}2{Fore.WHITE} Exit game\n\n"
                    )

            burnervar = input("Desired option: ")
            if burnervar.isdigit():
                blkjk_menu_state = int(burnervar)
                continue
            else:
                blkjk_menu_state = 10
                burnervar = 0
                continue
        elif blkjk_menu_state == 1: # playing ---

            counter = 0
            for _ in range(2): # nested loops to double deck size
                for s in suits:
                    for n in numbers:
                        deck1.collection[f"card{counter}"] = card(s, n)
                        counter += 1
            counter = 0
            deck1.order = [deck1.collection[f"card{c}"] for c in range(len(deck1.collection))]
            deck1.shuffle()

            dealer_hand = [deck1.order.pop(0) for _ in range(2)]
            player_hand = [deck1.order.pop(0) for _ in range(2)]
            clear()
            UI_top_bar()
            submenu_info("Blackjack")

            print(f"\n{Back.BLUE}{Fore.BLACK} Dealer's hand: \n")
            mult_cards_display(dealer_hand)

            print(f"\n\n{Back.BLUE}{Fore.BLACK} Your hand: \n")
            mult_cards_display(player_hand)
            break
            

        elif blkjk_menu_state == 2: # exit
            clear()
            blkjk_menu_state = 0
            menu_state = 0
            continue
        elif blkjk_menu_state == 10: # ERROR handler
            clear()
            UI_top_bar()
            submenu_info("Blackjack")
            print("\nInvalid input.")

            blkjk_menu_state = 0
            enter = input(f"\n\n{Fore.GREEN}ENTER{Style.RESET_ALL} = Try again")
            continue
        else:   # ERROR handler for any other numeric input
            clear()
            UI_top_bar()
            submenu_info("Blackjack")
            print("\nInvalid input.")

            blkjk_menu_state = 0
            enter = input(f"\n\n{Fore.GREEN}ENTER{Style.RESET_ALL} = Try again")
            continue


    elif menu_state == 10: # invalid input state
        clear()
        UI_top_bar()
        print("\nInvalid input.")
        menu_state = 0
        enter = input(f"\n\n{Fore.RED}ENTER{Style.RESET_ALL} = Try again")
        continue