import random


def create_card(rank:str,suite:str):
    # H, C, D, S.
    card = {'rank':rank, 'suite':suite, 'value':1}
    return card


def card_rank(num):
    if num == 11:
        return 'J'
    if num == 12:
        return 'Q'
    if num == 13:
        return 'K'
    else: return num



def build_standard_deck() -> list[dict]:
    cards_deck = []
    card_suite = ['H','C','D','S']
    
    for i in range(13):
        for j in range(4):
           cards_deck.append({"rank":card_rank(i+1) , 'suite': card_suite[j], "value":i+1})
    return cards_deck
    
    




def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    new_deck = deck 
    
    while swaps >= 0:
        random1 = random.randrange(0,52)    
        random2 = random.randrange(0,52)
        card1 = deck[random1]
        card2 = deck[random2]
        
        
        
        temp = new_deck[random1]
        if random1 == random2:
            continue
        
        if card2['suite'] == 'H':
            if card2['value'] % 5 != 0:
                continue
        elif card2['suite'] == 'C':
            if card2['value'] % 3 != 0:
                continue
        elif card2['suite'] == 'D':
            if card2['value'] % 2 != 0:
                continue 
        elif card2['suite'] == 'S':
            if card2['value'] % 7 != 0:
                continue   
        
        
        new_deck[random1] = new_deck[random2]
        new_deck[random2] = temp
        swaps -=1
    return new_deck
