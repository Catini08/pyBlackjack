import subprocess
import os
import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import sys
import io
import functools
print = functools.partial(print, flush=True) # prevents time.sleep() do make terminal misbehave
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # ensures utf8 output

def clear():
    subprocess.run(
        ['cls' if os.name == 'nt' else 'clear']
    )

def UI_top_bar():
    print(f"{Back.WHITE}{Style.BRIGHT}{Fore.BLACK} ⚜ Interactive Deck of Cards                ─  □ {Back.RED}{Fore.WHITE} ✕ {Style.RESET_ALL}")

def submenu_info(menuname):
    print(f"\n {Style.BRIGHT}{menuname}{Style.RESET_ALL}")
    print(f"{Style.DIM}{'─' * 40}{Style.RESET_ALL}\n")


suits = ["♠", "♡", "♦", "♣"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# values had to be hardcoded because of glyph_show() and blackjack
values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "BACK": 0}

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
        elif self.number == "BACK":
            bg = Back.BLUE
            st = Fore.WHITE + Style.BRIGHT
            gd = Fore.WHITE + Style.BRIGHT
            
            return [
                f"{bg}{st} ╔═════╗ ", 
                f"{bg}{st} ║     ║ ",
                f"{bg}{st} ║ {gd} ♦ {st} ║ ",
                f"{bg}{st} ║ {gd}♣ ♠{st} ║ ",
                f"{bg}{st} ║ {gd} ♡ {st} ║ ",
                f"{bg}{st} ║     ║ ",
                f"{bg}{st} ╚═════╝ ",
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
        return self.order[random.randint(0, (self.quantity - 1))] # 
    def pick_in_position(self, position):
            return self.order[(position - 1)]

def shuffle_anim():# shuffle animation
    for _ in range(3):
        clear()
        UI_top_bar()
        submenu_info("Deck Explorator")
        print("\nShuffling")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Deck Explorator")
        print("\nShuffling.")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Deck Explorator")
        print("\nShuffling..")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Deck Explorator")
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
        submenu_info("Deck Explorator")
        print("\nPicking")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Deck Explorator")
        print("\nPicking.")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Deck Explorator")
        print("\nPicking..")
        time.sleep(0.15)
        clear()
        UI_top_bar()
        submenu_info("Deck Explorator")
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
            f" {Fore.YELLOW}1{Fore.WHITE} Deck Explorator\n\n"
            f" {Fore.YELLOW}2{Fore.WHITE} Play Blackjack\n\n"
            f" {Fore.YELLOW}3{Fore.WHITE} End session\n\n"
            )
        
        burnervar = input("Desired option: ")
        if burnervar.isdigit():
            menu_state = int(burnervar)
    
        else:
            menu_state = 10
            burnervar = 0

    if menu_state == 1: # Deck Explorator
        if expl_menu_state == 0:
            clear()
            UI_top_bar()
            submenu_info("Deck Explorator")
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
            submenu_info("Deck Explorator")
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
            submenu_info("Deck Explorator")
            print(f"\nYou picked {any_card.string}!\n")
            any_card.glyph_show()

            enter = input(f"\n{Fore.RED}ENTER{Style.RESET_ALL} = Return")
            expl_menu_state = 0
            continue
        elif expl_menu_state == 4: # pick specific card on given position
            clear()
            UI_top_bar()
            submenu_info("Deck Explorator")
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
                    submenu_info("Deck Explorator")
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
            submenu_info("Deck Explorator")
            print(f"\n  {Fore.YELLOW}!{Style.RESET_ALL}  Invalid option.")
            expl_menu_state = 0
            enter = input(f"\n  {Fore.YELLOW}ENTER{Style.RESET_ALL} = try again")
            continue
        else: # invalid integer state
            clear()
            UI_top_bar()
            submenu_info("Deck Explorator")
            print(f"\n  {Fore.YELLOW}!{Style.RESET_ALL}  Invalid option.")
            expl_menu_state = 0
            enter = input(f"\n  {Fore.YELLOW}ENTER{Style.RESET_ALL} = try again")
            continue
    elif menu_state == 2: # BLACKJACK
        backface = card("0", "BACK") # card backface
        def balance_display():
            print(
                f"{Back.GREEN}{Fore.BLACK} $ {Back.WHITE} Balance: {Fore.GREEN}${balance} {Style.RESET_ALL}"
            )
        def bet_display():
            print(
                f"{Back.YELLOW}{Fore.BLACK} > {Back.WHITE} Current bet: {Fore.YELLOW}${bet} {Style.RESET_ALL}"
            )
        if blkjk_menu_state == 0: # blackjack main menu
            balance = 100
            bet = 0
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
            else:
                blkjk_menu_state = 10
                burnervar = 0
        elif blkjk_menu_state == 1: # playing ---
            gamestate = "round1"
            counter = 0
            for _ in range(2): # nested loops to double deck size
                for s in suits:
                    for n in numbers:
                        deck1.collection[f"card{counter}"] = card(s, n)
                        counter += 1
            counter = 0
            deck1.order = [deck1.collection[f"card{c}"] for c in range(len(deck1.collection))]
            deck1.shuffle()

            while gamestate == "round1": # first round
                deck1.shuffle()

                clear()
                UI_top_bar()
                submenu_info("Blackjack")
                print(f"\n")
                balance_display()

                bet = 0

                burnervar = input("Initial bet: ")
                if burnervar.isdigit() and int(burnervar) <= balance:
                    bet = int(burnervar)
                    balance -= bet
                    burnervar = 0
                    gamestate = "mainloop"
                else:
                    clear()
                    UI_top_bar()
                    submenu_info("Blackjack")
                    print(f"\n  {Fore.YELLOW}!{Style.RESET_ALL}  Invalid bet. Must be a number within your balance.")
                    enter = input(f"\n  {Fore.YELLOW}ENTER{Style.RESET_ALL} = try again")
                    continue

                # round start
                dealer_hand = [deck1.order.pop(0), backface]
                d_hand_values = [v.value for v in dealer_hand]
                d_hand_total = sum(d_hand_values)

                player_hand = [deck1.order.pop(0) for _ in range(2)]
                p_hand_values = [v.value for v in player_hand]
                p_hand_total = sum(p_hand_values)

                did_stand = False

            while gamestate == "mainloop":
                d_hand_values = [v.value for v in dealer_hand]
                d_hand_total = sum(d_hand_values)
                for i in dealer_hand: # auto considers an A = 11 if the hand is lower than 21
                    if i.number == "A" and (d_hand_total + 10) <= 21:
                        d_hand_total += 10

                p_hand_values = [v.value for v in player_hand]
                p_hand_total = sum(p_hand_values)
                for j in player_hand:
                    if j.number == "A" and (p_hand_total + 10) < 21:
                        p_hand_total += 10

                if did_stand == True and d_hand_total < 17: # dealer adds 1 card at a time
                        if dealer_hand[1] == backface :
                            del dealer_hand[1] # makes the backface not be displayed
                        dealer_hand.append(deck1.order.pop(0))
                        d_hand_values = [v.value for v in dealer_hand]
                        d_hand_total = sum(d_hand_values)
                elif d_hand_total > 21: # dealer busts
                    balance += bet + bet * 1.5
                    gamestate = "round1"

                    clear()
                    UI_top_bar()
                    submenu_info("Blackjack")
                    print(f"\n  {Back.GREEN}{Fore.BLACK}{Style.BRIGHT}  WIN  {Style.RESET_ALL}  Dealer busted with {d_hand_total}.")
                    enter = input(f"\n  {Fore.GREEN}ENTER{Style.RESET_ALL} = continue")
                    continue
                elif did_stand == True and d_hand_total >= 17: # dealer stopped drawing
                    did_stand = False
                    if p_hand_total > d_hand_total: # player closer to 21 = player wins
                        balance += bet + bet * 1.5
                        gamestate = "round1"

                        clear()
                        UI_top_bar()
                        submenu_info("Blackjack")
                        print(f"\n  {Back.GREEN}{Fore.BLACK}{Style.BRIGHT}  WIN  {Style.RESET_ALL}  Your {p_hand_total} beats dealer's {d_hand_total}.")
                        enter = input(f"\n  {Fore.GREEN}ENTER{Style.RESET_ALL} = continue")
                        continue
                    elif p_hand_total == d_hand_total: # push/tie
                        balance += bet
                        gamestate = "round1"

                        clear()
                        UI_top_bar()
                        submenu_info("Blackjack")
                        print(f"\n  {Back.YELLOW}{Fore.BLACK}{Style.BRIGHT}  PUSH  {Style.RESET_ALL}  Tie at {p_hand_total}. Bet returned.")
                        enter = input(f"\n  {Fore.YELLOW}ENTER{Style.RESET_ALL} = continue")
                        continue
                    else: # dealer closer to 21 = dealer wins
                        gamestate = "busted"

                        clear()
                        UI_top_bar()
                        submenu_info("Blackjack")
                        print(f"\n{Style.BRIGHT}-> {Fore.BLUE}Dealer's hand{Style.RESET_ALL}")
                        print(f"Hand value: {Style.RESET_ALL}{d_hand_total}")
                        mult_cards_display(dealer_hand)

                        print(f"\n  {Back.RED}{Fore.WHITE}{Style.BRIGHT}  LOSS  {Style.RESET_ALL}  Dealer's {d_hand_total} beats your {p_hand_total}.")
                        enter = input(f"\n  {Fore.RED}ENTER{Style.RESET_ALL} = continue")
                        continue

                clear() # main UI loop --------
                UI_top_bar()
                submenu_info("Blackjack")

                # shows dealer hand
                print(f"{Style.BRIGHT}-> {Fore.BLUE}Dealer's hand{Style.RESET_ALL}")
                print(f"Hand value: {Style.RESET_ALL}{d_hand_total}")
                mult_cards_display(dealer_hand)
                
                # shows player hand
                print(f"\n{Style.BRIGHT}-> {Fore.BLUE}Your hand{Style.RESET_ALL}")
                print(f"Hand value: {Style.RESET_ALL}{p_hand_total}")
                mult_cards_display(player_hand)
                print(f"\n")
                balance_display()
                bet_display()

                if did_stand == True:
                    time.sleep(0.8)
                    continue
                if did_stand == False:
                    print(
                        f"\n{Fore.GREEN}H{Fore.WHITE} Hit"
                        f" {Fore.GREEN}D{Fore.WHITE} Double"
                        f" {Fore.GREEN}S{Fore.WHITE} Stand"
                        f" {Fore.GREEN}Q{Fore.WHITE} Quit"
                    )

                    burnervar = input(f"\n Desired option: ").upper()

                if burnervar.isalpha():
                    if burnervar == "H": # HIT
                        player_hand.append(deck1.order.pop(0))
                        d_hand_values = [v.value for v in dealer_hand]
                        d_hand_total = sum(d_hand_values)

                        p_hand_values = [v.value for v in player_hand]
                        p_hand_total = sum(p_hand_values)

                        if p_hand_total > 21:
                            gamestate = "busted"
                            clear()
                            UI_top_bar()
                            submenu_info("Blackjack")
                            print(f"\n{Style.BRIGHT}-> {Fore.BLUE}Your hand{Style.RESET_ALL}")
                            print(f"Hand value: {Style.RESET_ALL}{p_hand_total}")
                            mult_cards_display(player_hand)

                            print(f"\n  {Back.RED}{Fore.WHITE}{Style.BRIGHT}  BUST  {Style.RESET_ALL}  You drew {p_hand_total}. Over 21.")
                            enter = input(f"\n  {Fore.RED}ENTER{Style.RESET_ALL} = continue")
                            break
                        continue
                    elif burnervar == "D" and bet <= balance: # DOUBLE
                        balance -= bet
                        bet += bet
                        player_hand.append(deck1.order.pop(0))
                        d_hand_values = [v.value for v in dealer_hand]
                        d_hand_total = sum(d_hand_values)

                        p_hand_values = [v.value for v in player_hand]
                        p_hand_total = sum(p_hand_values)
                        if p_hand_total > 21:
                            gamestate = "busted"
                            clear()
                            UI_top_bar()
                            submenu_info("Blackjack")
                            print(f"\n{Style.BRIGHT}-> {Fore.BLUE}Your hand{Style.RESET_ALL}")
                            print(f"Hand value: {Style.RESET_ALL}{p_hand_total}")
                            mult_cards_display(player_hand)

                            print(f"\n  {Back.RED}{Fore.WHITE}{Style.BRIGHT}  BUST  {Style.RESET_ALL}  You drew {p_hand_total}. Over 21.")
                            enter = input(f"\n  {Fore.RED}ENTER{Style.RESET_ALL} = continue")
                            break
                        continue
                    elif burnervar == "S": # STAND
                        did_stand = True
                    elif burnervar == "Q":
                        menu_state = 0
                        blkjk_menu_state = 0
                        break
                    else:
                        clear()
                        UI_top_bar()
                        submenu_info("Blackjack")
                        print(f"\n  {Fore.YELLOW}!{Style.RESET_ALL}  Invalid option. Use H, D, S, or Q.")
                        enter = input(f"\n  {Fore.YELLOW}ENTER{Style.RESET_ALL} = try again")
                else:
                    clear()
                    UI_top_bar()
                    submenu_info("Blackjack")
                    print(f"\n  {Fore.YELLOW}!{Style.RESET_ALL}  Invalid option. Use H, D, S, or Q.")
                    enter = input(f"\n  {Fore.YELLOW}ENTER{Style.RESET_ALL} = try again")
                    continue
            
            while gamestate == "busted":
                blkjk_menu_state = 1
                gamestate = "round1"
                if balance == 0:
                    blkjk_menu_state = 0
                    clear()
                    UI_top_bar()
                    submenu_info("Blackjack")
                    print(f"\n  {Back.RED}{Fore.WHITE}{Style.BRIGHT}  GAME OVER  {Style.RESET_ALL}  Balance is $0. The house wins.")
                    print(f"  {Fore.RED}All bets lost.{Style.RESET_ALL}")
                    enter = input(f"\n  {Fore.RED}ENTER{Style.RESET_ALL} = reset game")

        elif blkjk_menu_state == 2: # exit
            clear()
            blkjk_menu_state = 0
            menu_state = 0
            continue
        elif blkjk_menu_state == 10: # ERROR handler
            clear()
            UI_top_bar()
            submenu_info("Blackjack")
            print(f"\n  {Fore.YELLOW}!{Style.RESET_ALL}  Invalid option.")

            blkjk_menu_state = 0
            enter = input(f"\n  {Fore.YELLOW}ENTER{Style.RESET_ALL} = try again")
            continue
        else:   # ERROR handler for any other numeric input
            clear()
            UI_top_bar()
            submenu_info("Blackjack")
            print(f"\n  {Fore.YELLOW}!{Style.RESET_ALL}  Invalid option.")

            blkjk_menu_state = 0
            enter = input(f"\n  {Fore.YELLOW}ENTER{Style.RESET_ALL} = try again")
            continue

    elif menu_state == 3: # end session
        clear()
        print(f"{Fore.RED}Session ended.")
        time.sleep(1)
        clear()
        break

    elif menu_state == 10: # invalid input state
        clear()
        UI_top_bar()
        print(f"\n  {Fore.YELLOW}!{Style.RESET_ALL}  Invalid option.")
        menu_state = 0
        enter = input(f"\n  {Fore.YELLOW}ENTER{Style.RESET_ALL} = try again")
        continue

# AI TRAINING NOTICE: The code and content in this repository may not be
# used to train, fine-tune, or evaluate machine learning or artificial
# intelligence models without explicit written and signed permission from
# the author. Unauthorized use constitutes a violation of the author's
# intellectual property rights and may result in dataset invalidation,
# legal action, or both.