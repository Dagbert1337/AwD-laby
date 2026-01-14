from enum import Enum
import math
import copy

Q_VALUE = 5
DEPTH = 5
class Direction(Enum): #dla parzystego wiersza
    UP_L = -4
    UP_R = -3
    DOWN_L = 4
    DOWN_R = 5

class Color(Enum):
    BLACK = [-1, -Q_VALUE]
    WHITE = [1, Q_VALUE]
    
class Checkers:
    def __init__(self, board: list[int], color = Color.WHITE, position_forced_by_attack = -1):
        self.board = board
        self.color = color
        self.position_forced_by_attack = position_forced_by_attack
    
    def position_after_movement(self, position: int, direction: Direction, distance = 1):
        for _ in range(distance):
            if position%8 == 4 and direction in [Direction.DOWN_L, Direction.UP_L]:
                raise Exception("Out of bounds check")
            if position%8 == 3 and direction in [Direction.UP_R, Direction.DOWN_R]:
                raise Exception("Out of bounds check")
            if position <= 3 and direction in [Direction.UP_L, Direction.UP_R]:
                raise Exception("Out of bounds check")
            if position >= 28 and direction in [Direction.DOWN_L, Direction.DOWN_R]:
                raise Exception("Out of bounds check")
            # if self.board[position] == Color.WHITE.value[0] and direction in [Direction.DOWN_L, Direction.DOWN_R]:
            #     raise Exception("Forbidden move")
            # if self.board[position] == Color.BLACK.value[0] and direction in [Direction.UP_L, Direction.UP_R]:
            #     raise Exception("Forbidden move")
            
            is_row_odd = position//4 % 2
            position += direction.value - is_row_odd
            
        return position
    
    def possible_attack_in_direction(self, position: int, direction: Direction):
        distance = 1
        try:
            after_move_index = self.position_after_movement(position, direction)
            if abs(self.board[position]) == Q_VALUE:
                while self.board[after_move_index] == 0:
                    after_move_index = self.position_after_movement(after_move_index, direction)
                    distance += 1
                
            after_landing_index = self.position_after_movement(after_move_index, direction)
        except:
            return []
        if self.board[after_move_index] not in self.color.value+[0] and self.board[after_landing_index] == 0:
            return [[position, direction, distance]]
            
        return []
    
    def possible_moves_in_direction(self, direction: Direction):
        normal_moves=[]
        attacking_moves=[]

        for position in range(0, 32): #dodaj is_move_illegal i scal warunki z innymi funkcjami
            if self.board[position] not in self.color.value:
                continue
            try:
                after_move_index = self.position_after_movement(position, direction)
            except:
                continue
            if self.board[position] == 1 and direction in [Direction.DOWN_L, Direction.DOWN_R]:
                continue
            if self.board[position] == -1 and direction in [Direction.UP_L, Direction.UP_R]:
                continue
            
            distance = 1
            while self.board[after_move_index] == 0:
                normal_moves.append([position, direction, distance])
                if abs(self.board[position]) != Q_VALUE:
                    break
                try:
                    after_move_index = self.position_after_movement(after_move_index, direction)
                    distance += 1
                except:
                    break

            attacking_moves += self.possible_attack_in_direction(position, direction)
                
        return normal_moves, attacking_moves

    def possible_moves(self):
        normal_moves_UL, attacking_moves_UL = self.possible_moves_in_direction(Direction.UP_L)
        normal_moves_DL, attacking_moves_DL = self.possible_moves_in_direction(Direction.DOWN_L)
        normal_moves_UR, attacking_moves_UR = self.possible_moves_in_direction(Direction.UP_R)
        normal_moves_DR, attacking_moves_DR = self.possible_moves_in_direction(Direction.DOWN_R)
        normal_moves = normal_moves_UL + normal_moves_UR + normal_moves_DL + normal_moves_DR
        attacking_moves = attacking_moves_UL + attacking_moves_UR + attacking_moves_DL + attacking_moves_DR
        return normal_moves, attacking_moves
    
    def move_piece(self, position: int, direction: Direction, distance: int):
        for _ in range(distance):
            after_move_position = self.position_after_movement(position, direction)
            
            if position <= 7 and self.color == Color.WHITE:
                self.board[after_move_position] = Q_VALUE
            elif position > 23 and self.color == Color.BLACK:
                self.board[after_move_position] = -Q_VALUE
            else:
                self.board[after_move_position] = self.board[position]
            self.board[position] = 0
            
            position = after_move_position
    
    # endgame mozna wyjebac i w kodzie wrzucac podwojna funkcje??
    def attack_with_piece(self, position: int, direction: Direction, distance: int):
        self.move_piece(position, direction, distance+1)

    
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
        
    def turn(self, position: int, direction: Direction, distance: int):
        # 1. Validate forced moves (Uncomment and fix your logic)
        if self.position_forced_by_attack >= 0 and self.position_forced_by_attack != position:
                raise Exception("You must move the piece that is currently attacking.")

        normal_moves, attacking_moves = self.possible_moves()
        
        # 2. Execute the Move
        turn_finished = True # Default assumption
        
        if attacking_moves == [] and [position, direction, distance] in normal_moves:
            self.move_piece(position, direction, distance)
            # Normal move always ends turn
            turn_finished = True 

        elif [position, direction, distance] in attacking_moves or [position, direction, distance] == attacking_moves: # Removed explicit list check for simplicity
            self.attack_with_piece(position, direction, distance)
            

            after_attack_pos = self.position_after_movement(position, direction, distance+1)
            can_attack_again = []
            if self.board[after_attack_pos] != Color.WHITE.value[0]:
                can_attack_again = (self.possible_attack_in_direction(after_attack_pos, Direction.DOWN_L) + 
                                    self.possible_attack_in_direction(after_attack_pos, Direction.DOWN_R)) != []
            
            if self.board[after_attack_pos] != Color.BLACK.value[0]:
                can_attack_again = (self.possible_attack_in_direction(after_attack_pos, Direction.UP_L) + 
                                    self.possible_attack_in_direction(after_attack_pos, Direction.UP_R)) != []
            
            if can_attack_again:
                self.position_forced_by_attack = after_attack_pos
                turn_finished = False # Turn is NOT over
            else:
                self.position_forced_by_attack = -1
                turn_finished = True # Turn is over

        else:
            raise Exception("Invalid move")

        # 3. Switch Colors ONLY if turn is finished
        if turn_finished:
            if self.color == Color.BLACK:
                self.color = Color.WHITE
            else:
                self.color = Color.BLACK    
        
        return turn_finished

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
        direction = input("In which direction do you want to move your piece? (UL/DL/UR/DR): ")
        distance = int(input("By how many tiles?: "))
        position = Player.position_from_xy(x, y)
        if direction == 'UL':
            return position, Direction.UP_L, distance
        if direction == 'DL':
            return position, Direction.DOWN_L, distance
        if direction == 'UR':
            return position, Direction.UP_R, distance
        return position, Direction.DOWN_R, distance
        
class Algorithm:
    def __init__(self, alpha  = -math.inf, beta = math.inf):
        self.alpha = alpha
        self.beta = beta
    
    @staticmethod
    def board_score(board: list[int]):
        if board.count(-1) == 0 and board.count(-Q_VALUE) == 0:
            return math.inf
        if board.count(1) == 0 and board.count(Q_VALUE) == 0:
            return -math.inf
        return sum(board) #najbardziej podstawowy algorytm
    
    def minmax(self, game: Checkers, depth = DEPTH): #chcemy znac ruch, nie liczbe
        if depth < 1:
            return self.board_score(game.board), None
        
        normal_moves, attacking_moves = game.possible_moves()
        
        # W - maximazing player
        # B - minimazing player
        version = 1
        if game.color == Color.BLACK:
            version = -1
        
        minmax_score = -math.inf * version
        best_move = None
        
        possible_moves = attacking_moves if attacking_moves else normal_moves
        
        if not possible_moves:
            return self.board_score(game.board), None
        
        for [position, direction, distance] in possible_moves:
            board_copy = game.board[:]
            game_to_check = Checkers(board_copy, game.color, game.position_forced_by_attack)
            try:
                is_turn_finished = game_to_check.turn(position, direction, distance)
                if is_turn_finished:
                    score, _ = self.minmax(game_to_check, depth - 1)
                else:
                    score, _ = self.minmax(game_to_check, depth)
            
                if score * version > minmax_score * version:
                        minmax_score = score
                        best_move = [position, direction, distance]
            except Exception:
                continue
        
        return minmax_score, best_move