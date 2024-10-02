# chess/search.py

import math
from chess.evaluation import evaluate_board

# Define the function that will generate all possible legal moves for a given player.
# You can assume that the function `generate_legal_moves(board, color)` exists and returns
# a list of possible moves where each move is represented as a tuple of (start_pos, end_pos).
from chess.move_generator import generate_legal_moves

# Define infinity to represent large positive and negative values
INFINITY = math.inf

def minimax(board, depth, alpha, beta, is_maximizing_player, color, endgame=False):
    """
    Minimax algorithm with alpha-beta pruning and depth limitation.

    Args:
        board (list): The current state of the chessboard.
        depth (int): The depth limit for the search.
        alpha (float): The best value that the maximizer can guarantee.
        beta (float): The best value that the minimizer can guarantee.
        is_maximizing_player (bool): True if it's the maximizing player's turn (white), False if it's the minimizing player's turn (black).
        color (str): 'white' or 'black', representing the current player's color.
        endgame (bool): True if it's an endgame position.

    Returns:
        (float, tuple): The best evaluation score and the best move (start_pos, end_pos).
    """
    # Base case: depth is 0 or the game is over (no legal moves or checkmate)
    if depth == 0:
        return evaluate_board(board, endgame), None

    legal_moves = generate_legal_moves(board, color)
    if not legal_moves:
        return evaluate_board(board, endgame), None

    # Initialize best_move as None
    best_move = None

    if is_maximizing_player:
        max_eval = -INFINITY
        for move in legal_moves:
            # Make the move (assume the function make_move(board, move) exists)
            new_board = make_move(board, move)
            eval, _ = minimax(new_board, depth - 1, alpha, beta, False, 'black', endgame)

            # Undo the move (assume the function undo_move(board, move) exists)
            # undo_move(board, move)

            if eval > max_eval:
                max_eval = eval
                best_move = move

            # Alpha-beta pruning
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff, prune the rest of the branch

        return max_eval, best_move

    else:  # Minimizing player (black's turn)
        min_eval = INFINITY
        for move in legal_moves:
            # Make the move
            new_board = make_move(board, move)
            eval, _ = minimax(new_board, depth - 1, alpha, beta, True, 'white', endgame)

            # Undo the move
            # undo_move(board, move)

            if eval < min_eval:
                min_eval = eval
                best_move = move

            # Alpha-beta pruning
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff, prune the rest of the branch

        return min_eval, best_move


def make_move(board, move):
    """
    Applies the move to the board and returns the new board state.
    This function should modify the board in-place or return a copy of the board with the move applied.

    Args:
        board (list): The current state of the chessboard.
        move (tuple): The move to apply, represented as (start_pos, end_pos).

    Returns:
        list: The new board state after the move is applied.
    """
    new_board = [row[:] for row in board]  # Create a deep copy of the board
    start_pos, end_pos = move
    piece = new_board[start_pos[0]][start_pos[1]]
    new_board[end_pos[0]][end_pos[1]] = piece
    new_board[start_pos[0]][start_pos[1]] = None  # The starting square becomes empty

    return new_board


def search_best_move(board, depth, is_white_turn, endgame=False):
    """
    Searches for the best move using Minimax with Alpha-Beta pruning.

    Args:
        board (list): The current state of the chessboard.
        depth (int): The depth limit for the search.
        is_white_turn (bool): True if it's white's turn, False if it's black's turn.
        endgame (bool): True if it's an endgame position.

    Returns:
        tuple: The best move (start_pos, end_pos).
    """
    if is_white_turn:
        best_eval, best_move = minimax(board, depth, -INFINITY, INFINITY, True, 'white', endgame)
    else:
        best_eval, best_move = minimax(board, depth, -INFINITY, INFINITY, False, 'black', endgame)
    
    return best_eval, best_move