import random
import time


def start_game():  # Run the game
    print("\n" * 100)
    dealer_hand = []
    player_hand = []
    player_total = 0
    dealer_total = 0
    dealers_first_card = get_card()  # Get starting card for dealer
    players_first_card = get_card()  # Get starting card for player

    # Add to the players total points for first card at the start
    split_list = GetValuesOfCards(players_first_card) # Declare class call
    result = split_list.convert_to_int()  # Change the string into int e.g. King = 12
    player_total = player_total + result  # Add to players total

    # Add to the dealers total points for first card at the start
    split_list = GetValuesOfCards(dealers_first_card)
    result = split_list.convert_to_int()  # Change the string into int e.g. King = 12
    dealer_total = dealer_total + result  # Add to dealers total

    players_first_card_value = GetValuesOfCards(players_first_card)  # Convert the card value e.g. King =14
    players_first_card_value = players_first_card_value.convert_to_int()

    dealers_first_card_value = GetValuesOfCards(dealers_first_card)  # Convert the card value e.g. King =14
    dealers_first_card_value = dealers_first_card_value.convert_to_int()

    dealer_hand.append(dealers_first_card_value)  # Add dealers first card value to hand
    player_hand.append(players_first_card_value)  # Add players first card to hand

    print(f"You start with {players_first_card}")
    print(f"The dealer starts with {dealers_first_card}\n")

    print(f"Players Score is: {player_total}")
    print(f"Dealer Score is: {dealer_total}")

    while True:
        question = input("\nHit or Pass: ")
        if question == "Hit":
            players_new_card = players_draw()   # Call a new card for the player
            print(f"You have drawn {players_new_card}\n")
            player_card_value = GetValuesOfCards(players_new_card)  # Get the value of the card e.g. King = 13
            player_card_value = player_card_value.convert_to_int()
            player_hand.append(player_card_value)

            player_total = add_list(player_hand)  # Add to the players score
            player_hand = check_score(player_total, player_hand)  # Check if player wins or busts
            player_total = add_list(player_hand)
            print(f"Players Score is: {player_total}")
            print(f"Dealer Score is: {dealer_total}")

            if player_total > 21:
                print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!Players Score is: {player_total}")
                bust("Player Bust! Dealer Wins!")
        elif question == "Pass":
            print("\n")
            while player_total > dealer_total < 21:
                print("Hit")
                dealers_new_card = players_draw()
                print(f"The dealer has drawn {dealers_new_card}\n")
                dealers_card_value = GetValuesOfCards(dealers_new_card)  # Get the value of the card e.g. King = 13
                dealers_card_value = dealers_card_value.convert_to_int()
                dealer_hand.append(dealers_card_value)
                #print(f"dealers_card_value = {dealers_card_value}")
                #print(f"dealer_hand = {dealer_hand}")

                dealer_total = add_list(dealer_hand)  # Add to the players score
                dealer_hand = check_score(dealer_total, dealer_hand)  # Check if player wins or busts
                dealer_total = add_list(dealer_hand)

                print(f"Players Score is: {player_total}")
                print(f"Dealer Score is: {dealer_total}")

                time.sleep(2)
            if dealer_total > 21:
                bust("Dealer Bust! Player Wins!")
            elif dealer_total > player_total <= 21:
                winner("Dealer Wins")
            elif dealer_total == player_total:
                draw("Its a draw")

        else:
            print("\n")


def play_again():
    while True:
        ask = input("Play again Y/N ?")
        if ask == "Y":
            start_game()
        if ask == "N":
            print("Good Bye")
            exit()

def add_list(player_hand):
    b = sum(player_hand)
    return b


def check_score(total, hand):
    if total == 21:
        winner("Player Wins")
    elif total > 21:
        for ace in hand:
            if ace == 14:
                hand.remove(ace)
                hand.append(1)
                print("Ace too low\n")
                print(f"New hand is {hand}")
                return hand
            else:
                continue
        return hand
    else:
        return hand


def players_draw():  # Players card is called
    a_new_card = give_card()
    a_new_card = str(a_new_card)[2:-2]  # [''] are removed
    return a_new_card


def computers_turn():
    print("Computers turn")
    exit()


def winner(win):
    print(f"{win}")
    play_again()


def bust(win):
    print(f"{win}")
    play_again()


def draw(win):
    print(win)
    play_again()


def get_card():  # Gen a random card and return it
    card = give_card()
    card = str(card)[2:-2]
    return card


def player_draw():
    question = input("Hit or Pass? : ")
    if question == "Hit":
        print("\n"*100)
        the_card = get_card()
        print(f"You drew {the_card}")
        return the_card
    else:
        return False


class Deck:  # Generate the deck
    def __init__(self):
        self.suit = {"Heart", "Diamond", "Clubs", "Spade"}
        self.values = {2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"}
        self.deck = []

    def build_deck(self):
        for i in self.suit:
            for n in self.values:
                results = {f"{n} of {i}"}
                self.deck.append(results)
        return self.deck  # Return the deck


def give_card():  # Pick a random card from the list Deck
    test = Deck()
    the_deck = test.build_deck()
    result = random.choice(the_deck)
    return result


class GetValuesOfCards:
    def __init__(self, card):
        self.playerNumber = 0
        self.card = card

    def convert_to_int(self):
        self.playerNumber = 0
        value = self.card.split(' ', 1)[0]
        if value == "Ace":
            self.playerNumber = self.playerNumber + 11
            return int(self.playerNumber)
        elif value == "King":
            self.playerNumber = self.playerNumber + 10
            return int(self.playerNumber)
        elif value == "Queen":
            self.playerNumber = self.playerNumber + 10
            return int(self.playerNumber)
        elif value == "Jack":
            self.playerNumber = self.playerNumber + 10
            return int(self.playerNumber)
        else:
            self.playerNumber = int(value)
            return int(self.playerNumber)


start_game()  # Start