import random
import os

from board import Board  # Import the class from the other file
from human_player import Human_player
from player import Player
from monte_carlo_player import Monte_carlo_player



#os clearing
def clear():
    #clear the terminal based on os used
    os.system("cls" if os.name in ('nt', 'dos') else "clear")


def refresh_gamestate(board):
    clear()
    board.print_board()

def choose_players(board):
    player = []
    #lambda for delaying object creation
    choices = {
        "1": lambda: Human_player(board),
        "2": lambda: Player(board),
        "3": lambda: Monte_carlo_player(board,250),
        "4": lambda: Monte_carlo_player(board,750),
        "5": lambda: Monte_carlo_player(board,1500)
    }
    
    while len(player) < 2:

        print(f"""Select Player {len(player) + 1}:
    1. Human (same machine)
    2. Randobot
    3. Normal AI
    4. Hard AI
    5. Impossible AI         
e/exit: stop playing
""")
        choice = input(f"Select Player {len(player) + 1}: ").strip().lower()
        if choice == "e" or choice == "exit":
            return False
        if choice in choices:
            player.append(choices[choice]())
            clear()
        else:
            print("Invalid choice.")
    return player

def play_game():
    print("\nStarting new game... \n")
    game_board = Board()
    player = choose_players(game_board)
    if player == False:
        return False  # exit
    
    starting_turn = [0,1]
    random.shuffle(starting_turn)
    turn_order = dict(zip(['X', 'O'], starting_turn)) 
    turn_index = turn_order[game_board.get_current_turn()]
    
    #Clear this info
    refresh_gamestate(game_board)
    while True:
        print(f"{game_board.get_current_turn()}'s turn: \n")

        desired_move = player[turn_index].get_move()

        if desired_move == "e":
            break
            
        if type(desired_move) is int: 
            if game_board.is_move_valid(desired_move):

                game_board.play_move(desired_move)
                turn_index = turn_order[game_board.get_current_turn()]
                player[turn_index].update_board(game_board)
                winner = game_board.check_game_win()

                refresh_gamestate(game_board)


                if winner == "draw":
                    print("Tie!")
                    break

                if winner != None:
                    print(winner + " Wins!")
                    break
    
    return input("Play again? (y/n): ").strip().lower().startswith("y")

    
while play_game():
    continue

