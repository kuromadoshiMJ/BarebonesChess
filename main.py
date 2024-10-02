from chess.board import setup_initial_board, print_board
from chess.search import search_best_move, make_move
from chess.move_generator import generate_legal_moves
# from chess.pieces import Piece

def main():
    # Step 1: Initialize the chessboard
    chess_board = setup_initial_board()
    print("Initial Board:")
    print_board(chess_board)
    # Step 2: Set up game loop
    is_white_turn = True  # Start with white's turn
    move_count = 0
    max_depth = 3  # Depth-limited search

    while True:
        # Display the current player's turn
        if is_white_turn:
            print("\nWhite's move:")
        else:
            print("\nBlack's move:")

        # Step 3: Generate and search for the best move using Minimax
        best_eval, best_move = search_best_move(chess_board, depth=max_depth, is_white_turn=is_white_turn)

        if not best_move:
            print("No legal moves available!")
            if is_white_turn:
                print("Black wins!")
            else:
                print("White wins!")
            break

        # Step 4: Apply the best move to the board
        start_pos, end_pos = best_move
        print(f"Best move: {start_pos} -> {end_pos}")

        # Update the board with the best move
        chess_board = make_move(chess_board, best_move)

        # Print the updated board
        print_board(chess_board)
        # Step 5: Check for game-ending conditions (e.g., checkmate, stalemate)
        legal_moves = generate_legal_moves(chess_board, 'white' if is_white_turn else 'black')
        if not legal_moves:
            if is_white_turn:
                print("Black wins!")
            else:
                print("White wins!")
            break

        # Step 6: Switch turns
        is_white_turn = not is_white_turn
        move_count += 1

        # Optionally limit the number of moves for testing purposes
        if move_count >= 20:
            print("Game ended due to move limit.")
            break

if __name__ == "__main__":
    main()