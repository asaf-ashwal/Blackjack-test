from .player_io import ask_player_action, add_card


def calculate_hand_rank(hand: list[dict]) -> int:
    sum = 0
    for i in hand:
        num = handle_value(i)
        if num == 1:
            if sum + 14 < 21:
                sum += 14 
            else:  sum += 1
        else: sum += int(num)
    return str(sum)
   

def handle_value(card):
    if not card['rank'].isdigit():
        return 10
    else: return int(card['rank'])


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    add_card(deck,player)
    add_card(deck,dealer) 


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        if int(calculate_hand_rank(dealer['hand'])) > 17:
            return True
        add_card(deck,dealer)
        if int(calculate_hand_rank(dealer['hand']))>21:
            print('LOST: ',dealer)
            return False


def victory(dealer,player):
    player_sum = calculate_hand_rank(player['hand'])
    dealer_sum = calculate_hand_rank(dealer['hand'])
    if player_sum > dealer_sum:
        print(f"!!!!  player won with sum of {player_sum} !!!!")
    elif player_sum < dealer_sum:
        print(f"!!!!  dealer won with sum of {dealer_sum} !!!!")
    else:
        print(f"!!!!  its a tie  with sum of {dealer_sum}!!!!")
        


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    
    deal_two_each(deck, player, dealer )
    while True:
        print('your sum is: ',calculate_hand_rank(player['hand']))
        player_enswer = ask_player_action()
        if player_enswer == 'H':
            add_card(deck,player)
            if int(calculate_hand_rank(player['hand']))>21:
                print (f'!!! you lost with sum of {calculate_hand_rank(player['hand'])} !!!')
                return None
        else: break
        
    dealer_play(deck,dealer)
    victory(dealer,player)
    return None
        