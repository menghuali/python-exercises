from classes import Card, Deck, Player


def play():
    p1 = Player('A')
    p2 = Player('B')

    deck = Deck()
    deck.shuffle()

    split_cards(deck, p1, p2)

    while continue_game(p1, p2):
        next_round(p1, p2)

    call_winner(p1, p2)


def split_cards(deck: Deck, p1: Player, p2: Player):
    while deck.has_more_cards():
        p1.add_cards(deck.deal_one())
        p2.add_cards(deck.deal_one())


def continue_game(p1: Player, p2: Player) -> bool:
    return p1.has_more_cards() and p2.has_more_cards()


def next_round(p1: Player, p2: Player) -> Player:
    if not continue_game(p1, p2):
        return None

    round_winner = None
    card1 = p1.remove_one()
    card2 = p2.remove_one()
    if card1.value > card2.value:
        round_winner = p1
    elif card1.value == card2.value:
        round_winner = next_round(p1, p2)
    else:
        round_winner = p2

    if round_winner == p1:
        round_winner.add_cards([card1, card2])
    elif round_winner == p2:
        round_winner.add_cards([card2, card1])

    return round_winner


def call_winner(p1: Player, p2: Player):
    if p1.has_more_cards():
        print(f'Winner is {p1}')
    elif p2.has_more_cards():
        print(f'Winner is {p2}')
    else:
        print('No winners')


play()
