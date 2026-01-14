from classes import Color, Direction, Player, Checkers, Algorithm

def turn(game: Checkers):
    position, direction = Player.user_input(game)
    
    # #### exception handling ####
    # if game.position_forced_by_attack >= 0 and game.position_forced_by_attack != position:
    #     raise Exception
    # ############################
    
    normal_moves, attacking_moves = game.possible_moves()
    if attacking_moves == [] and [position, direction] in normal_moves:
        game.move_piece(position, direction)
    elif [position, direction] in attacking_moves or [position, direction] == attacking_moves:
        game.attack_with_piece(position, direction)
        after_attack_position = game.position_after_movement(game.position_after_movement(position, direction), direction)
        if game.possible_attack_in_direction(after_attack_position, Direction.LEFT) + game.possible_attack_in_direction(after_attack_position, Direction.RIGHT) != []:
            game.position_forced_by_attack = after_attack_position
            return turn(game)
        game.position_forced_by_attack = -1
        
    # ### exception handling ###
    # else:
    #     raise Exception
    # ##########################
    if game.color == Color.BLACK:
        game.color = Color.WHITE
    else:
        game.color = Color.BLACK    
    
    return game
    
TURNS = 10
REPEATS = 3

def main():
    game = Checkers()
    # for _ in range(TURNS):
    #     for _ in range(REPEATS):
    #         try:
    #             game = turn(game)
    #             break
    #         except:
    #             print("You cannot make that move, try again")

    
    alg = Algorithm()
    turns = int(input())
    print(alg.minmax(game, turns))


if __name__ == '__main__':
    main()