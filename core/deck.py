import random
from .game_logic import handle_value


def create_card(rank:str,suite:str):
    # H, C, D, S.
    card = {'rank':rank, 'suite':suite,}
    return card


def card_rank(num):
    if num == '11':
        return 'J'
    if num == '12':
        return 'Q'
    if num == '13':
        return 'K'
    else: return num



def build_standard_deck() -> list[dict]:
    cards_deck = []
    card_suite = ['H','C','D','S']
    
    for i in range(13):
        for j in range(4):
           cards_deck.append({"rank":card_rank(str(i+1)) , 'suite': card_suite[j],})
    return cards_deck
    
    




def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    new_deck = deck 
    while swaps >= 0:
        random1 = deck[random.randrange(0,52)]
        random2 = deck[random.randrange(0,52)]
        r1 = random1['suite']
        r2 = random2['suite']
        if r2 == r1:
            continue
        if r2 == 'H':
            print('h')
            if side_handle(random2['rank']) % 5 != 0:
                continue
        elif r2 == 'C':
            print('c')
            if side_handle(random2['rank']) % 3 != 0:
                continue        
        elif r2 == 'D':
            print('d')
            if side_handle(random2['rank']) % 2 != 0:
                continue
        elif r2 == 'S':
            print('s')
            if side_handle(random2['rank']) % 7 != 0:
                continue
        temp = random1
        new_deck[side_handle(random1['rank'])] = new_deck[side_handle(random2['rank'])]
        new_deck[side_handle(random2['rank'])] = temp
        swaps -= 1
    return new_deck

def side_handle(card):
    if  card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    else: return int(card)