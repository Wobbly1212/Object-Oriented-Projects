import random

# Define suits, ranks, and values of the cards
suits = ("Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
          "J": 10, "Q": 10, "K": 10, "A": 11}

# Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck Class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

# Hand Class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # Track Aces for adjusting value

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "A":
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        # If value is over 21 and there is an Ace, count Ace as 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

# Game Logic
def play_blackjack():
    while True:
        print("\nWelcome to Blackjack!\n")
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        # Initial dealing
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        # Show initial hands
        print(f"Your hand: {player_hand} (Value: {player_hand.value})")
        print(f"Dealer's hand: {dealer_hand.cards[0]}, [Hidden]")

        # Player's turn
        while player_hand.value < 21:
            action = input("Do you want to Hit (h) or Stay (s)? ").lower()
            if action == "h":
                player_hand.add_card(deck.deal_card())
                print(f"\nYour hand: {player_hand} (Value: {player_hand.value})")
                if player_hand.value > 21:
                    print("You busted! Dealer wins.")
                    break
            elif action == "s":
                break
            else:
                print("Invalid choice! Please enter 'h' or 's'.")

        # Dealer's turn
        if player_hand.value <= 21:
            print(f"\nDealer reveals hand: {dealer_hand} (Value: {dealer_hand.value})")
            while dealer_hand.value < 17:
                dealer_hand.add_card(deck.deal_card())
                print(f"Dealer hits: {dealer_hand} (Value: {dealer_hand.value})")

            if dealer_hand.value > 21:
                print("Dealer busted! You win!")
            elif dealer_hand.value > player_hand.value:
                print("Dealer wins!")
            elif dealer_hand.value < player_hand.value:
                print("You win!")
            else:
                print("It's a tie!")

        # Ask to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    play_blackjack()