def is_on_board(x, y):
    """ Check if the coordinates are within the bounds of the chessboard. """
    return 0 <= x < 8 and 0 <= y < 8


def generate_pawn_moves(board, x, y):
    """ Generate legal moves for a pawn. """
    piece = board[x][y]
    moves = []
    direction = 1 if piece.color == 'white' else -1  # White moves up (-1), black moves down (+1)
    
    # Forward movement
    if is_on_board(x + direction, y) and board[x + direction][y] is None:
        moves.append((x + direction, y))
        # Double move on the first turn
        if (piece.color == 'white' and x == 6) or (piece.color == 'black' and x == 1):
            if board[x + 2 * direction][y] is None:
                moves.append((x + 2 * direction, y))
    
    # Capture moves (diagonal left and right)
    for dy in [-1, 1]:
        if is_on_board(x + direction, y + dy) and board[x + direction][y + dy] is not None:
            if board[x + direction][y + dy].color != piece.color:
                moves.append((x + direction, y + dy))
    
    return moves


def generate_knight_moves(board, x, y):
    """ Generate legal moves for a knight. """
    moves = []
    piece = board[x][y]
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    for dx, dy in knight_moves:
        new_x, new_y = x + dx, y + dy
        if is_on_board(new_x, new_y):
            if board[new_x][new_y] is None or board[new_x][new_y].color != piece.color:
                moves.append((new_x, new_y))
    
    return moves


def generate_bishop_moves(board, x, y):
    """ Generate legal moves for a bishop. """
    moves = []
    piece = board[x][y]
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        while is_on_board(new_x, new_y) and board[new_x][new_y] is None:
            moves.append((new_x, new_y))
            new_x, new_y = new_x + dx, new_y + dy
        # Capture an opponent's piece
        if is_on_board(new_x, new_y) and board[new_x][new_y].color != piece.color:
            moves.append((new_x, new_y))
    
    return moves


def generate_rook_moves(board, x, y):
    """ Generate legal moves for a rook. """
    moves = []
    piece = board[x][y]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        while is_on_board(new_x, new_y) and board[new_x][new_y] is None:
            moves.append((new_x, new_y))
            new_x, new_y = new_x + dx, new_y + dy
        # Capture an opponent's piece
        if is_on_board(new_x, new_y) and board[new_x][new_y].color != piece.color:
            moves.append((new_x, new_y))
    
    return moves


def generate_queen_moves(board, x, y):
    """ Generate legal moves for a queen. """
    # Queen can move like a rook and a bishop
    return generate_rook_moves(board, x, y) + generate_bishop_moves(board, x, y)


def generate_king_moves(board, x, y):
    """ Generate legal moves for a king. """
    moves = []
    piece = board[x][y]
    king_moves = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    for dx, dy in king_moves:
        new_x, new_y = x + dx, y + dy
        if is_on_board(new_x, new_y):
            if board[new_x][new_y] is None or board[new_x][new_y].color != piece.color:
                moves.append((new_x, new_y))
    
    # Castling (to be implemented later)
    
    return moves

def generate_legal_moves(board, color):
    """
    Generates all legal moves for the given color (either 'white' or 'black').

    Args:
        board (list): The current state of the chessboard.
        color (str): The player's color ('white' or 'black').

    Returns:
        list of tuples: Each move is represented as a tuple (start_pos, end_pos),
                        where start_pos and end_pos are (row, col) positions.
    """
    legal_moves = []

    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            if piece is None or piece.color != color:
                continue  # Skip empty squares or pieces of the opposite color

            # Generate moves based on the type of piece
            if piece.piece_type == 'P':  # Pawn
                moves = generate_pawn_moves(board, x, y)
            elif piece.piece_type == 'N':  # Knight
                moves = generate_knight_moves(board, x, y)
            elif piece.piece_type == 'B':  # Bishop
                moves = generate_bishop_moves(board, x, y)
            elif piece.piece_type == 'R':  # Rook
                moves = generate_rook_moves(board, x, y)
            elif piece.piece_type == 'Q':  # Queen
                moves = generate_queen_moves(board, x, y)
            elif piece.piece_type == 'K':  # King
                moves = generate_king_moves(board, x, y)
            else:
                moves = []  # No moves if the piece is unrecognized

            # Convert piece-specific moves to the format (start_pos, end_pos)
            start_pos = (x, y)
            for end_pos in moves:
                legal_moves.append((start_pos, end_pos))

    return legal_moves