class Piece:
    def __init__(self, piece_type, color):
        self.piece_type = piece_type  # e.g., 'P' for pawn, 'R' for rook
        self.color = color  # 'white' or 'black'

    def __repr__(self):
        # Represent the piece as a string, lowercase for black, uppercase for white
        if self.color == 'white':
            return self.piece_type.upper()  # White pieces in uppercase
        else:
            return self.piece_type.lower()  # Black pieces in lowercase