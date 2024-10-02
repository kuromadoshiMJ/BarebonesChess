# chess/board.py
from chess.pieces import Piece
from chess.move_generator import (
    generate_pawn_moves,
    generate_knight_moves,
    generate_bishop_moves,
    generate_rook_moves,
    generate_queen_moves,
    generate_king_moves,
)
# from chess.pieces.py import Piece

# Function to create an empty 8x8 chessboard
def create_empty_board():
    return [[None for _ in range(8)] for _ in range(8)]


# Function to set up the initial board configuration
def setup_initial_board():
    board = create_empty_board()

    # Set up pawns
    for i in range(8):
        board[1][i] = Piece('P', 'white')  # White pawns
        board[6][i] = Piece('P', 'black')  # Black pawns

    # Set up rooks
    board[0][0] = board[0][7] = Piece('R', 'white')  # White rooks
    board[7][0] = board[7][7] = Piece('R', 'black')  # Black rooks

    # Set up knights
    board[0][1] = board[0][6] = Piece('N', 'white')  # White knights
    board[7][1] = board[7][6] = Piece('N', 'black')  # Black knights

    # Set up bishops
    board[0][2] = board[0][5] = Piece('B', 'white')  # White bishops
    board[7][2] = board[7][5] = Piece('B', 'black')  # Black bishops

    # Set up queens
    board[0][3] = Piece('Q', 'white')  # White queen
    board[7][3] = Piece('Q', 'black')  # Black queen

    # Set up kings
    board[0][4] = Piece('K', 'white')  # White king
    board[7][4] = Piece('K', 'black')  # Black king

    return board

# def make_move(board, move):
#     """
#     Applies the given move to the board and returns the new board state.
    
#     Args:
#         board (list): The current state of the chessboard.
#         move (tuple): The move to apply, represented as (start_pos, end_pos).
    
#     Returns:
#         list: The new board state after the move is applied.
#     """
#     # Unpack the start and end positions from the move
#     start_pos, end_pos = move
#     start_x, start_y = start_pos
#     end_x, end_y = end_pos

#     # Copy the current board state to avoid mutating the original board
#     new_board = [row[:] for row in board]  # Deep copy of the board

#     # Get the piece to move
#     moving_piece = new_board[start_x][start_y]

#     # Apply the move (move the piece to the new position)
#     new_board[end_x][end_y] = moving_piece
#     new_board[start_x][start_y] = None  # Empty the starting square

#     # Handle promotion (for pawns reaching the last rank)
#     if moving_piece.piece_type == 'P':
#         if (moving_piece.color == 'white' and end_x == 0) or (moving_piece.color == 'black' and end_x == 7):
#             # Promote the pawn to a queen (this can be extended to handle other promotions)
#             new_board[end_x][end_y] = Piece('Q', moving_piece.color)

#     # Castling and en passant can be handled here if needed (to be implemented)

#     return new_board

# Function to print the chessboard
def print_board(board):
    for row in board:
        print(' '.join([str(piece) if piece else '.' for piece in row]))

# def generate_legal_moves(board, x, y):
#     piece = board[x][y]
#     if piece is None:
#         return []

#     if piece.piece_type == 'P':
#         return generate_pawn_moves(board, x, y)
#     elif piece.piece_type == 'N':
#         return generate_knight_moves(board, x, y)
#     elif piece.piece_type == 'B':
#         return generate_bishop_moves(board, x, y)
#     elif piece.piece_type == 'R':
#         return generate_rook_moves(board, x, y)
#     elif piece.piece_type == 'Q':
#         return generate_queen_moves(board, x, y)
#     elif piece.piece_type == 'K':
#         return generate_king_moves(board, x, y)
#     return []
board = setup_initial_board()

if __name__ == "__main__":
    print_board(board)
