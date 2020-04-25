'''
52 card deck
remove a card from the deck and deal to player
deal to pc
hit or stay
Append value to list to find ace if it goes over 21
win/lose/bust
plat again
'''
import random

def add_list():
    b = sum(players_hand)
    return b

def win():
    print("Winner")
    exit()

def lose():
    print("Bust")
    exit()


class Deck:
    def __init__(self):
        self.suit = {"Heart", "Diamond", "Clubs", "Spade"}
        self.values = {2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"}
        self.deck = []

    def build_deck(self):
        for i in self.suit:
            for n in self.values:
                results = {f"{n} of {i}"}
                self.deck.append(results)
        return self.deck


class DealCards:
    def __init__(self):
        self.test = Deck()
        self.the_deck = []
        self.result = []

    def build_hand(self):
        test = Deck()
        the_deck = test.build_deck()
        self.result = random.choice(the_deck)
        return self.result


class PlayerHand:
    def __init__(self):
        self.ask_for_cards = ""

    def hit_or_miss(self):
        self.ask_for_cards = input("Hit or Pass: ")
        if self.ask_for_cards == "Hit":
            return deal_card(self.ask_for_cards)
        else:
            #print("Pass")
            return False

def deal_card(ask_for_cards):
    newtest = DealCards()
    if ask_for_cards == "Hit":
        called_card = newtest.build_hand()
        res = str(called_card)[2:-2]
        #print(f"Your drew the {res}")
        return res


class CheckValues:
    def __init__(self,card):
        self.playerNumber = 0
        self.card = card

    def convert_to_int(self):
        self.playerNumber = 0
        value = self.card.split(' ', 1)[0]
        if (value == "Ace"):
            self.playerNumber = self.playerNumber + 14
            return int(self.playerNumber)
        elif (value == "King"):
            self.playerNumber = self.playerNumber + 13
            return int(self.playerNumber)
        elif (value == "Queen"):
            self.playerNumber = self.playerNumber + 12
            return int(self.playerNumber)
        elif (value == "Jack"):
            self.playerNumber = self.playerNumber + 11
            return int(self.playerNumber)
        else:
            self.playerNumber = int(value)
            return int(self.playerNumber)


class AddPlayerHand:
    def __init__(self,list_of_cards):
        self.list_of_cards = list_of_cards
        self.new_array = {}

    def ace_to_low(self):
        for ace in players_hand:
            if ace == 14:
                players_hand.remove(ace)
                players_hand.append(1)
                break
        print("Ace too low\n")
        return self.list_of_cards


class AI_turn():
    def __init__(self):
        pass

    def first_draw(self):
        return deal_card("Hit")

    def ai_turn(self):
        pass


total_in_player_hand = 0
the_flag = 0

players_hand = []
dealers_hand = []
hand_test = PlayerHand()


def read_the_dealers_hand():
    dealers_first_card = AI_turn()
    dealers_hand = dealers_first_card.first_draw()
    print(f"Dealers first card = {dealers_hand}")
    check = CheckValues(dealers_hand)
    store_value = check.convert_to_int()
    return store_value


def players_the_dealers_hand():
    check = CheckValues(the_card_name)
    return check.convert_to_int()  # Change the string to a int


def check_score(sumOfList, players_hand):
    if sumOfList == 21:
        win()
    elif sumOfList > 21:
        if players_hand.__contains__(14):
            change_to_low = AddPlayerHand(players_hand)
            players_hand = change_to_low.ace_to_low()
            print(f"Players Hand = {players_hand}")
            sumOfList = add_list()
            print(f"Your score is:{sumOfList}\n")
        else:
            lose()


def add_to_dealers_hand():
    the_drawn_card = deal_card("Hit")
    return the_drawn_card

while True:
    if the_flag == 0:
        result = read_the_dealers_hand()
        dealers_hand.append(result)
        the_flag = 1

    print(f"Dealers hand: {dealers_hand}\n")
    the_card_name = hand_test.hit_or_miss()  # Ask and return user input
    if not the_card_name:
        card = add_to_dealers_hand()
        print(f"The dealer drew: {card}")


    print(f"You drew: {the_card_name}")
    store_value = players_the_dealers_hand()
    players_hand.append(store_value)
    print(f"Players Hand = {players_hand}")
    adding = AddPlayerHand(players_hand)
    sumOfList = add_list()
    print(f"Your score is:{sumOfList}\n")
    check_score(sumOfList,players_hand)