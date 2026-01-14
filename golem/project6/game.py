from classes import Player, Checkers, Heuristics, Algorithm
from collections.abc import Callable
    
TURNS = 50

def clash(func1: Callable[[list[int]], float], func2: Callable[[list[int]], float], board = [-1]*12 + [0]*8 + [1]*12):
    game = Checkers(board)   
    player_w, player_b, depth = Player.settings()
    alg_w = Algorithm(func1)
    alg_b = Algorithm(func2)
        
    for _ in range(TURNS):
        # --- Player 1's Turn ---
        if player_w == '1':
            Player.handle_player(game)
        else:
            while True:
                _, move = alg_w.minmax(game, depth)
                if move is None:
                    print("Black won!")
                    return 2                
                finished = game.turn(move[0], move[1], move[2])
                if finished: break
        
        game.print_board()
        if not any(piece < 0 for piece in game.board):
            print("White won!")
            return 1
        
        # --- Player 2's Turn ---
        if player_b == '1':
            Player.handle_player(game)
        else:
            while True:
                _, move = alg_b.minmax(game, depth)
                if move is None:
                    print("White won!")
                    return 1
                finished = game.turn(move[0], move[1], move[2])
                if finished: break

        game.print_board()
        if not any(piece > 0 for piece in game.board):
            print("Black won!")
            return 2
            
    print("Ah, draw...")
    return 3

def main():
    heuristic = Heuristics(0.3)
    clash(heuristic.sum_and_doubling, heuristic.sum_score)
    

if __name__ == '__main__':
    main()