# This file does not import raylib. Students can test these functions without
# opening a game window. The board is a list of lists of one-character strings.

# Keep these values and use them in your code below.
MOVE_COST = 1
TRAP_PENALTY = 3
POTION_BONUS = 8
COIN_POINTS = 100


def is_valid_move(board, row, col):
    if row < 0 or col < 0:
        return False

    try: 
        space = board[row][col]
    except IndexError:
        return False

    if board[row][col] == '#':
        return False

    return True

def move_player(board, player, direction):
    if player["moves"] <= 0:
        return False

    if direction == "LEFT":
        move_row = player["row"] 
        move_col = player["col"] - 1
    elif direction == "RIGHT":
        move_row = player["row"] 
        move_col = player["col"] + 1
    elif direction == "DOWN":
        move_row = player["row"] + 1
        move_col = player["col"] 
    elif direction == "UP":
        move_row = player["row"] - 1
        move_col = player["col"] 
    else: 
        return False

    if not is_valid_move(board, move_row, move_col):
        return False

    player["row"] = move_row
    player["col"] = move_col
    player["moves"] -= MOVE_COST

    return True


def collect_item(board, player):
    board_item = board[player["row"]][player["col"]] 

    if board_item == "G":
        player["gold"] += 1
        player["score"] += COIN_POINTS
        board[player["row"]][player["col"]] = "."
        return "G"

    if board_item == "M":
        player["moves"] += POTION_BONUS
        board[player["row"]][player["col"]]  = "."
        return "M"
    
    if board_item == "K":
        player["keys"] += 1
        board[player["row"]][player["col"]]  = "."
        return "K"

    return None

def check_trap(board, player):
    board_item = board[player["row"]][player["col"]] 

    if board_item == "T":
        player["moves"] -= TRAP_PENALTY
        board[player["row"]][player["col"]]  = "."
        return True

    return False


def has_won(board, player):
    if board[player["row"]][player["col"]]  != "V":
        return False

    if player["keys"] != player["total_keys"]:
        return False
    return True