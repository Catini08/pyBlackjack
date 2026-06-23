# Interactive Deck of Cards

## Key Technical Decisions

### Dynamic card collection within the Deck Explorator
Creating a dynamic collection made it possible for anyone to easily edit the **suits** and **numbers** lists. This way, one can make a card range from A to 20, or add an extra suit of their liking. All cards are created upon a variable of class Deck() being stated.

### Pop-based dealing
The deck system uses pop(0) to mimic the real-life action of picking the topmost card when manipulating a deck. It pops from the main self.order list from the deck class and stores the card inside either the dealer or player hands, which are also lists.

### Doubled deck for Blackjack
The doubled deck is a standard in Blackjack, as well as using the Anglo-American deck. This is why the card collection is hardcoded for the Blackjack section of the code.

### Ace flexibility
Whenever a player draws an Ace, its value is auto-promoted to 11 if the player hand total value is lower than 21 after the promotion. The Ace is demoted automatically too, because the total hand values are updated every turn.

### Card back as a card object
To be loyal to standard Blackjack, I hardcoded an instance of the card class with number="BACK" to be displayed whenever the player hasn't chosen to Stand. The instance has self.value = 0, and the number name "BACK" is used by the glyph function. It vanishes whenever the player chooses to stand.

---

## Challenges

### Rendering multiple cards side-by-side
The original card glyph generator was a one-card-only function that would display the face of any card in the deck. It was useful for the Deck Explorator, but not for Blackjack. I ended up changing it to a function that returns every line of the glyph, so they can be stored into a list and then printed by mult_cards_display(cardfaces), where **cardfaces** is always a list of card instances.

### Ace value auto-promotion
This was one of the challenges that scared me the most in the beginning, but ended up being fairly fast to solve once I sat down to think about it. I decided to solve it not by changing the Ace value, but by adding 10 to the player/dealer hand total whenever there is an Ace in it. As the hand value is calculated every turn based on the individual card values, this addition is not permanent, and only takes place when the hand doesn't bust upon adding.

### Managing Blackjack balance and bet values
The Blackjack game and rules introduced a wide set of variables to the code, despite being a simple card game. A fair challenge was storing the player's balance between turns. A bug I faced was that when the player would win or lose, their balance would reset to 100. I later fixed it by only initializing the player's balance when the Main Screen of Blackjack was shown, and not every round.

---

## What I Would Do Differently

* Managing the finite states using only while loops instead of ifs and elses. This would make the core more readable.
* Using the Questionary Python library to handle player choices rather than listening to raw user input. This would eliminate the many error handlers throughout the code. (May happen in a future update)
* Nesting UI features inside fewer, more robust functions. The repetition of the same three commands at every UI update is not optimal in my opinion.