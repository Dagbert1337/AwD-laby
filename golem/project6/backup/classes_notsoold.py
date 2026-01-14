from enum import Enum
import math
import copy

Q_VALUE = 5
DEPTH = 5
class Direction(Enum):
    LEFT = -1
    RIGHT = 1

class Color(Enum):
    BLACK = [-1, -Q_VALUE]
    WHITE = [1, Q_VALUE]
    
class Checkers:
    def __init__(self, board = [-1]*12 + [0]*8 + [1]*12, color = Color.WHITE, position_forced_by_attack = -1):
        self.board = board
        self.color = color
        self.position_forced_by_attack = position_forced_by_attack
    
    def position_after_movement(self, position: int, direction: Direction):
        is_row_odd = position//4 % 2
        if self.color == Color.WHITE:
            if direction == Direction.LEFT:
                return position - 4 - is_row_odd
            return position - 4 - is_row_odd + 1
        if direction == Direction.LEFT:
            return position + 4 - is_row_odd
        return position + 4 - is_row_odd + 1
    
    def possible_attack_in_direction(self, position: int, direction: Direction):
        if (position%8 in [0, 4] and direction == Direction.LEFT) or (position%8 in [3, 7] and direction == Direction.RIGHT):
            return []
        if self.color == Color.WHITE and position <= 7:
            return []
        if self.color == Color.BLACK and position >= 24:
            return []
        after_move_index = self.position_after_movement(position, direction)
        if self.board[after_move_index] not in self.color.value+[0] and self.board[self.position_after_movement(after_move_index, direction)] == 0:
                return [[position, direction]]
        return []
    
    def possible_moves_in_direction(self, direction: Direction):
        normal_moves=[]
        attacking_moves=[]
        if self.color == Color.WHITE:
            start = 4
            end = 32
        else:
            start = 0
            end = 28
        for position in range(start, end):
            if (direction == Direction.LEFT and position%8 == 4) or (direction == Direction.RIGHT and position%8 == 3):
                continue
            if self.board[position] not in self.color.value:
                continue
            if self.board[self.position_after_movement(position, direction)] == 0:
                normal_moves.append([position, direction])
            attacking_moves += self.possible_attack_in_direction(position, direction)
        return normal_moves, attacking_moves

    def possible_moves(self):
        normal_moves_L, attacking_moves_L = self.possible_moves_in_direction(Direction.LEFT)
        normal_moves_R, attacking_moves_R = self.possible_moves_in_direction(Direction.RIGHT)
        normal_moves = normal_moves_L + normal_moves_R
        attacking_moves = attacking_moves_R + attacking_moves_L
        return normal_moves, attacking_moves
    
    def move_piece(self, position: int, direction: Direction):
        if (position%8 == 4 and direction == Direction.LEFT) or (position%8 == 3 and direction == Direction.RIGHT):
            #tu bylo wczesniej raise Exception
            #nwm czy ta zmiana czegos nie psuje
            return
        
        after_move_position = self.position_after_movement(position, direction)
        if position <= 7 and self.color == Color.WHITE:
            self.board[after_move_position] = Q_VALUE
        elif position > 23 and self.color == Color.BLACK:
            self.board[after_move_position] = -Q_VALUE
        else:
            self.board[after_move_position] = self.board[position]
        self.board[position] = 0

    ## stara wersja
    # def attack_with_piece(self, position: int, direction: Direction): 
    #     position_after_move = self.position_after_movement(position, direction)
    #     self.board[self.position_after_movement(position_after_move, direction)] = self.board[position]
    #     self.board[position_after_move] = 0
    #     self.board[position] = 0
    #     return self
    
    # endgame mozna wyjebac i w kodzie wrzucac podwojna funkcje??
    def attack_with_piece(self, position: int, direction: Direction):
        self.move_piece(position, direction)
        self.move_piece(self.position_after_movement(position, direction), direction)

    
    def print_board(self):
        print("\n    1 2 3 4 5 6 7 8")
        print("   -----------------")
        for row in range(8):
            row_str = f"{row + 1} |"
            for col in range(8):
                if (row + col) % 2 == 1:
                    index = row * 4 + col // 2
                    piece = self.board[index]
                    if piece == 1:
                        row_str += " w"
                    elif piece == Q_VALUE:
                        row_str += " W"
                    elif piece == -1:
                        row_str += " b"
                    elif piece == -Q_VALUE:
                        row_str += " B"
                    else:
                        row_str += " ." 
                else:
                    row_str += "  " 
            print(row_str + " |")
        print("   -----------------")
        
    def turn(self, position: int, direction: Direction):
        # #### exception handling ####
        # if game.position_forced_by_attack >= 0 and game.position_forced_by_attack != position:
        #     raise Exception
        # ############################
        
        normal_moves, attacking_moves = self.possible_moves()
        if attacking_moves == [] and [position, direction] in normal_moves:
            self.move_piece(position, direction)
        elif [position, direction] in attacking_moves or [position, direction] == attacking_moves:
            self.attack_with_piece(position, direction)
            after_attack_position = self.position_after_movement(self.position_after_movement(position, direction), direction)
            if self.possible_attack_in_direction(after_attack_position, Direction.LEFT) + self.possible_attack_in_direction(after_attack_position, Direction.RIGHT) != []:
                self.position_forced_by_attack = after_attack_position
                return self.turn() # a) bierzemy input od nowa; b) sprawdzamy wszystkie mozliwosci dla nowego ustawienia
            self.position_forced_by_attack = -1
            
        # ### exception handling ###
        # else:
        #     raise Exception
        # ##########################
        if self.color == Color.BLACK:
            self.color = Color.WHITE
        else:
            self.color = Color.BLACK    
        
        return self

class Player:
    @staticmethod
    def position_from_xy(x: int, y: int):
        return (y-1)*4 + (x-1)//2
    
    @staticmethod
    def user_input(game: Checkers): # to-do: trzeba sprawdzic czy wejscie jest poprawne
        game.print_board()
        if game.color == Color.WHITE:
            print("WHITE'S TURN")
        else:
            print("BLACK'S TURN")
        x = int(input("Enter the X coordinate: "))
        y = int(input("Enter the Y coordinate: "))
        direction = input("Where do you want to move your piece? (L/R): ")
        position = Player.position_from_xy(x, y)
        if direction == 'L':
            return position, Direction.LEFT
        return position, Direction.RIGHT
        
class Algorithm:
    def __init__(self, alpha  = -math.inf, beta = math.inf):
        self.alpha = alpha
        self.beta = beta
    
    @staticmethod
    def board_score(board: list):
        if board.count(-1) == 0 and board.count(-Q_VALUE) == 0:
            return math.inf
        if board.count(1) == 0 and board.count(Q_VALUE) == 0:
            return -math.inf
        return sum(board) #najbardziej podstawowy algorytm
    
    def minmax(self, game: Checkers, depth = DEPTH):
        if depth < 1:
            return self.board_score(game.board)
        
        normal_moves, attacking_moves = game.possible_moves()
        # print(normal_moves, attacking_moves)
        version = 1
        if game.color == Color.BLACK:
            version = -1
        
        minmax_score = -math.inf * version
            
        if attacking_moves == []:
            for [position, direction] in normal_moves:
                game_to_check = copy.deepcopy(game)
                game_to_check.move_piece(position, direction)
                if game_to_check.color == Color.WHITE:
                    game_to_check.color = Color.BLACK
                else:
                    game_to_check.color = Color.WHITE
                calc_score = self.minmax(game_to_check, depth - 1)
                
                if calc_score*version > minmax_score*version:
                    minmax_score = calc_score
            return minmax_score
        for [position, direction] in attacking_moves:
            game_to_check = copy.deepcopy(game)
            game_to_check.attack_with_piece(position, direction)
            after_attack_position = game_to_check.position_after_movement(game_to_check.position_after_movement(position, direction), direction)
            if game_to_check.possible_attack_in_direction(after_attack_position, Direction.LEFT) + game_to_check.possible_attack_in_direction(after_attack_position, Direction.RIGHT) != []:
                game_to_check.position_forced_by_attack = after_attack_position
                calc_score = self.minmax(game_to_check, depth)
            else:
                if game_to_check.color == Color.WHITE:
                    game_to_check.color = Color.BLACK
                else:
                    game_to_check.color = Color.WHITE
                game_to_check.position_forced_by_attack = -1
                calc_score = self.minmax(game_to_check, depth - 1)
            if calc_score*version > minmax_score*version:
                minmax_score = calc_score
        return minmax_score