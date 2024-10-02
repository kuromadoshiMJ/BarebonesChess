import pygame
from chess.board import setup_initial_board, print_board
from chess.move_generator import generate_legal_moves
from chess.search import search_best_move, make_move
# from chess.move_generator import make_move

# Initialize pygame
pygame.init()

# Constants for the chessboard GUI
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 640  # 8x8 chessboard (80x80 per square)
SQUARE_SIZE = SCREEN_WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (106, 159, 181)
DARK_BROWN = (181, 136, 99)
LIGHT_BROWN = (240, 217, 181)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess Engine GUI")
def load_and_scale_image(path):
    """ Load and scale the piece image to fit the board square. """
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (int(SQUARE_SIZE * 0.75), int(SQUARE_SIZE * 0.75)))

# Load piece images (You will need to have chess piece images for this to work)
PIECE_IMAGES = {
    "P": load_and_scale_image("assets/w_pawn_2x_ns.png"),  # White pawn
    "R": load_and_scale_image("assets/w_rook_2x_ns.png"),  # White rook
    "N": load_and_scale_image("assets/w_knight_2x_ns.png"),  # White knight
    "B": load_and_scale_image("assets/w_bishop_2x_ns.png"),  # White bishop
    "Q": load_and_scale_image("assets/w_queen_2x_ns.png"),  # White queen
    "K": load_and_scale_image("assets/w_king_2x_ns.png"),  # White king
    "p": load_and_scale_image("assets/b_pawn_2x_ns.png"),  # Black pawn
    "r": load_and_scale_image("assets/b_rook_2x_ns.png"),  # Black rook
    "n": load_and_scale_image("assets/b_knight_2x_ns.png"),  # Black knight
    "b": load_and_scale_image("assets/b_bishop_2x_ns.png"),  # Black bishop
    "q": load_and_scale_image("assets/b_queen_2x_ns.png"),  # Black queen
    "k": load_and_scale_image("assets/b_king_2x_ns.png"),  # Black king
}

def draw_board():
    """ Draws the chessboard on the screen. """
    colors = [LIGHT_BROWN, DARK_BROWN]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(board):
    """ Draws the pieces on the board based on the current state of the game. """
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece is not None:
                piece_img = PIECE_IMAGES[piece.piece_type.lower() if piece.color == 'black' else piece.piece_type.upper()]
                screen.blit(piece_img, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def pos_to_coord(mouse_pos):
    """ Convert mouse click position to board coordinates (row, col). """
    x, y = mouse_pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE

def main():
    # Initialize the chessboard
    chess_board = setup_initial_board()
    
    selected_square = None  # Store the square that is clicked first (piece selection)
    player_turn = 'white'  # White starts the game

    running = True
    while running:
        draw_board()
        draw_pieces(chess_board)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = pos_to_coord(pygame.mouse.get_pos())
                print(row, col)
                if selected_square:
                    print("this")
                    # Try to make the move
                    move = (selected_square, (row, col))
                    legal_moves = generate_legal_moves(chess_board, player_turn)
                    
                    print(legal_moves)
                    if move in legal_moves:
                        print("yes")
                        chess_board = make_move(chess_board, move)
                        player_turn = 'black' if player_turn == 'white' else 'white'
                    selected_square = None
                else:
                    print("that")
                    # Select a piece to move
                    piece = chess_board[row][col]
                    if piece is not None and piece.color == player_turn:
                        selected_square = (row, col)

        # AI move for black
        if player_turn == 'black':
            best_eval, best_move = search_best_move(chess_board, depth=3, is_white_turn=False)
            chess_board = make_move(chess_board, best_move)
            player_turn = 'white'

    pygame.quit()

if __name__ == "__main__":
    main()
