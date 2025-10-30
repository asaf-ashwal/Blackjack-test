from core.deck import build_standard_deck, shuffle_by_suit
from core.game_logic import run_full_game,calculate_hand_rank



if __name__ == "__main__":
    player = {"hand": [ ]}
    dealer = {"hand": [ ]}
    deck = build_standard_deck()
    shuffle_by_suit(deck)
    print(deck)
    run_full_game(deck, player, dealer)