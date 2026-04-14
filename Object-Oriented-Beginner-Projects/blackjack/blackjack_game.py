import random

suits = ("Spades", "Clubs", "Hearts", "Diamonds")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
          "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # Count of aces in the hand

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "A":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def play_blackjack():
    # Initialize and shuffle deck
    deck = Deck()
    deck.shuffle()

    # Create player and dealer hands
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal two cards to player and dealer
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Adjust for any aces in initial hands
    player_hand.adjust_for_ace()
    dealer_hand.adjust_for_ace()

    # Show initial hands
    print("\nDealer's showing card:", dealer_hand.cards[1])
    print("Player's hand:", ", ".join(str(card) for card in player_hand.cards))
    print("Player's total:", player_hand.value)

    # Player's turn: allow Hit or Stay until player chooses to stay or busts
    while True:
        choice = input("Would you like to Hit or Stay? (h/s): ").lower()
        if choice == 'h':
            player_hand.add_card(deck.deal())
            player_hand.adjust_for_ace()
            print("Player's hand:", ", ".join(str(card) for card in player_hand.cards))
            print("Player's total:", player_hand.value)
            if player_hand.value > 21:
                print("Player busts! Dealer wins.")
                return
        elif choice == 's':
            break
        else:
            print("Invalid choice. Please choose 'h' for Hit or 's' for Stay.")

    # Dealer's turn: reveal hidden card and hit until reaching 17 or higher
    print("\nDealer's hand:", ", ".join(str(card) for card in dealer_hand.cards))
    print("Dealer's total:", dealer_hand.value)

    while dealer_hand.value < 17:
        print("Dealer hits.")
        dealer_hand.add_card(deck.deal())
        dealer_hand.adjust_for_ace()
        print("Dealer's hand:", ", ".join(str(card) for card in dealer_hand.cards))
        print("Dealer's total:", dealer_hand.value)
        if dealer_hand.value > 21:
            print("Dealer busts! Player wins.")
            return

    # Compare final totals to determine the outcome
    print("\nFinal Results:")
    if dealer_hand.value > player_hand.value:
        print("Dealer wins!")
    elif dealer_hand.value < player_hand.value:
        print("Player wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    while True:
        play_blackjack()
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

