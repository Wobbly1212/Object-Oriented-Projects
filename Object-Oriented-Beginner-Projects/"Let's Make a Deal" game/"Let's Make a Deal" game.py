import random

# The Door class represents a single door in the game.
class Door:
    def __init__(self, number, prize):
        self.number = number      # The door's identifier (1, 2, or 3)
        self.prize = prize        # The prize behind the door ("car" or "goat")
        self.is_open = False      # Indicates whether the door is open or closed

    def reveal(self):
        """Open the door and return the prize."""
        self.is_open = True
        return self.prize

    def __str__(self):
        """Return a string representation of the door."""
        if self.is_open:
            return f"Door {self.number}: {self.prize}"
        else:
            return f"Door {self.number}: [Closed]"

def play_game():
    # Randomly assign prizes to doors
    prizes = ['car', 'goat', 'goat']
    random.shuffle(prizes)
    doors = [Door(i+1, prize) for i, prize in enumerate(prizes)]

    # Display the closed doors to the player
    print("There are 3 doors. Behind one door is a car; behind the other two, goats.")
    for door in doors:
        print(door)

    # Player selects a door
    while True:
        try:
            choice = int(input("Choose a door (1, 2, or 3): "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
    player_choice = choice

    # The computer (host) reveals a door with a goat from the unchosen doors
    remaining_doors = [door for door in doors if door.number != player_choice]
    goat_doors = [door for door in remaining_doors if door.prize == 'goat']
    door_to_reveal = random.choice(goat_doors)
    door_to_reveal.reveal()
    print("\nThe host opens one door to reveal a goat:")
    print(door_to_reveal)

    # Ask the player whether they want to switch to the remaining closed door
    while True:
        switch = input("\nDo you want to switch to the other closed door? (y/n): ").lower()
        if switch in ['y', 'n']:
            break
        else:
            print("Please enter 'y' or 'n'.")

    if switch == 'y':
        # Switch: choose the only remaining closed door that was not picked originally
        final_choice = [door for door in doors if door.number != player_choice and not door.is_open][0]
    else:
        # Stay with the original choice
        final_choice = [door for door in doors if door.number == player_choice][0]

    print("\nYour final choice is:")
    # Reveal the final choice and return whether it's a win (i.e. contains a car)
    final_prize = final_choice.reveal()
    print(final_choice)
    return final_prize == 'car'

def main():
    games_played = 0
    wins = 0
    while True:
        print("\n----- New Game -----")
        if play_game():
            print("Congratulations! You won the car!")
            wins += 1
        else:
            print("Sorry, you got a goat!")
        games_played += 1

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    # Report the game statistics when the player quits
    print(f"\nTotal games played: {games_played}")
    print(f"Total wins (car): {wins}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
