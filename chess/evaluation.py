# chess/evaluation.py

# Piece values for material evaluation
PIECE_VALUES = {
    'P': 1,   # Pawn
    'N': 3,   # Knight
    'B': 3,   # Bishop
    'R': 5,   # Rook
    'Q': 9,   # Queen
    'K': 0    # King (no material value, but we'll include for safety)
}

# Positional values for pawns
PAWN_POSITION_SCORES = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [5, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 2, 3, 3, 2, 1, 1],
    [0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5],
    [0, 0, 0, 2, 2, 0, 0, 0],
    [0.5, -0.5, -1, 0, 0, -1, -0.5, 0.5],
    [0.5, 1, 1, -2, -2, 1, 1, 0.5],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Positional values for knights
KNIGHT_POSITION_SCORES = [
    [-5, -4, -3, -3, -3, -3, -4, -5],
    [-4, -2, 0, 0, 0, 0, -2, -4],
    [-3, 0, 1, 1.5, 1.5, 1, 0, -3],
    [-3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3],
    [-3, 0, 1.5, 2, 2, 1.5, 0, -3],
    [-3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3],
    [-4, -2, 0, 0.5, 0.5, 0, -2, -4],
    [-5, -4, -3, -3, -3, -3, -4, -5]
]

# Positional values for bishops
BISHOP_POSITION_SCORES = [
    [-2, -1, -1, -1, -1, -1, -1, -2],
    [-1, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, 0.5, 1, 1, 0.5, 0, -1],
    [-1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1],
    [-1, 0, 1, 1, 1, 1, 0, -1],
    [-1, 1, 1, 1, 1, 1, 1, -1],
    [-1, 0.5, 0, 0, 0, 0, 0.5, -1],
    [-2, -1, -1, -1, -1, -1, -1, -2]
]

# Positional values for rooks
ROOK_POSITION_SCORES = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 1, 1, 1, 1, 1, 1, 0.5],
    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [0, 0, 0, 0.5, 0.5, 0, 0, 0]
]

# Positional values for queens
QUEEN_POSITION_SCORES = [
    [-2, -1, -1, -0.5, -0.5, -1, -1, -2],
    [-1, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1],
    [-0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
    [0, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
    [-1, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1],
    [-1, 0, 0.5, 0, 0, 0, 0, -1],
    [-2, -1, -1, -0.5, -0.5, -1, -1, -2]
]

# Positional values for kings (middle game)
KING_MIDDLE_POSITION_SCORES = [
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-2, -3, -3, -4, -4, -3, -3, -2],
    [-1, -2, -2, -2, -2, -2, -2, -1],
    [2, 2, 0, 0, 0, 0, 2, 2],
    [2, 3, 1, 0, 0, 1, 3, 2]
]

# Positional values for kings (endgame)
KING_ENDGAME_POSITION_SCORES = [
    [-5, -4, -3, -2, -2, -3, -4, -5],
    [-3, -2, -1, 0, 0, -1, -2, -3],
    [-3, -1, 2, 3, 3, 2, -1, -3],
    [-3, -1, 3, 4, 4, 3, -1, -3],
    [-3, -1, 3, 4, 4, 3, -1, -3],
    [-3, -1, 2, 3, 3, 2, -1, -3],
    [-3, -3, 0, 0, 0, 0, -3, -3],
    [-5, -3, -3, -3, -3, -3, -3, -5]
]

def evaluate_board(board, endgame=False):
    """
    Evaluates the current position on the board for both material and position.
    
    Positive score favors white, negative score favors black.
    """
    total_evaluation = 0

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece is not None:
                piece_value = get_piece_value(piece, row, col, endgame)
                if piece.color == 'white':
                    total_evaluation += piece_value
                else:
                    total_evaluation -= piece_value

    return total_evaluation


def get_piece_value(piece, row, col, endgame=False):
    """
    Returns the value of the piece, including its positional score.
    """
    piece_type = piece.piece_type.upper()  # Use uppercase to represent all pieces
    material_value = PIECE_VALUES.get(piece_type, 0)

    # Positional value
    if piece_type == 'P':
        position_value = PAWN_POSITION_SCORES[row][col]
    elif piece_type == 'N':
        position_value = KNIGHT_POSITION_SCORES[row][col]
    elif piece_type == 'B':
        position_value = BISHOP_POSITION_SCORES[row][col]
    elif piece_type == 'R':
        position_value = ROOK_POSITION_SCORES[row][col]
    elif piece_type == 'Q':
        position_value = QUEEN_POSITION_SCORES[row][col]
    elif piece_type == 'K':
        if endgame:
            position_value = KING_ENDGAME_POSITION_SCORES[row][col]
        else:
            position_value = KING_MIDDLE_POSITION_SCORES[row][col]
    else:
        position_value = 0  # Other pieces can be added here with their tables

    # Combine material and positional value
    return material_value + position_value


# Example usage:
# board = setup_initial_board()  # Assuming you have this function
# score = evaluate_board(board)
# print("Board evaluation:", score)
