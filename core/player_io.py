def ask_player_action() -> str:
    while True:
        result = input('to get Get another card Press H Stop the Press S: ')
        if result == 'S' or result == 'H':
            return result
        print('Invalid selection')
            
def add_card(deck, player):
    player['hand'].append(deck.pop())