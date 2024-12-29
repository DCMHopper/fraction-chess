import unittest
from board import Board
from agents import GenericAgent
from piece import Piece

class TestPieceMovement(unittest.TestCase):
    def setUp(self):
        self.board = Board()  # Board is hardcoded to 8x8
        # Clear the board for our tests
        for i in range(self.board.size):
            for j in range(self.board.size):
                self.board.field[i][j].piece = None
        self.white_agent = GenericAgent(self.board, 'white')
        self.black_agent = GenericAgent(self.board, 'black')

    def test_rook_basic_movement(self):
        # Place a white rook in the middle of an empty board
        self.board.field[3][3].piece = Piece('r', 'white')
        valid_moves = self.white_agent.check_moves(3, 3)
        
        # Rook should be able to move in all four directions
        expected_moves = set([
            # Horizontal moves
            (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7),
            # Vertical moves
            (0, 3), (1, 3), (2, 3), (4, 3), (5, 3), (6, 3), (7, 3)
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_rook_blocked_by_friendly(self):
        # Place a white rook with friendly pieces blocking
        self.board.field[3][3].piece = Piece('r', 'white')
        self.board.field[3][5].piece = Piece('p', 'white')  # Friendly piece to right
        self.board.field[5][3].piece = Piece('p', 'white')  # Friendly piece below
        
        valid_moves = self.white_agent.check_moves(3, 3)
        expected_moves = set([
            # Horizontal moves (right blocked at 5)
            (3, 0), (3, 1), (3, 2), (3, 4),
            # Vertical moves (down blocked at 5)
            (0, 3), (1, 3), (2, 3), (4, 3)
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_rook_capture(self):
        # Place a white rook with enemy pieces
        self.board.field[3][3].piece = Piece('r', 'white')
        self.board.field[3][5].piece = Piece('p', 'black')  # Enemy piece to right
        self.board.field[5][3].piece = Piece('p', 'black')  # Enemy piece below
        
        valid_moves = self.white_agent.check_moves(3, 3)
        expected_moves = set([
            # Horizontal moves (including capture at 5)
            (3, 0), (3, 1), (3, 2), (3, 4), (3, 5),
            # Vertical moves (including capture at 5)
            (0, 3), (1, 3), (2, 3), (4, 3), (5, 3)
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_bishop_basic_movement(self):
        # Place a white bishop in the middle of an empty board
        self.board.field[3][3].piece = Piece('b', 'white')
        valid_moves = self.white_agent.check_moves(3, 3)
        
        # Bishop should be able to move in all four diagonal directions
        expected_moves = set([
            # Northwest diagonal
            (2, 2), (1, 1), (0, 0),
            # Northeast diagonal
            (2, 4), (1, 5), (0, 6),
            # Southwest diagonal
            (4, 2), (5, 1), (6, 0),
            # Southeast diagonal
            (4, 4), (5, 5), (6, 6), (7, 7)
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_bishop_blocked_by_friendly(self):
        # Place a white bishop with friendly pieces blocking
        self.board.field[3][3].piece = Piece('b', 'white')
        self.board.field[1][1].piece = Piece('p', 'white')  # Friendly piece Northwest
        self.board.field[5][5].piece = Piece('p', 'white')  # Friendly piece Southeast
        
        valid_moves = self.white_agent.check_moves(3, 3)
        expected_moves = set([
            # Northwest diagonal (blocked at 1,1)
            (2, 2),
            # Northeast diagonal
            (2, 4), (1, 5), (0, 6),
            # Southwest diagonal
            (4, 2), (5, 1), (6, 0),
            # Southeast diagonal (blocked at 5,5)
            (4, 4)
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_bishop_capture(self):
        # Place a white bishop with enemy pieces
        self.board.field[3][3].piece = Piece('b', 'white')
        self.board.field[1][1].piece = Piece('p', 'black')  # Enemy piece Northwest
        self.board.field[5][5].piece = Piece('p', 'black')  # Enemy piece Southeast
        
        valid_moves = self.white_agent.check_moves(3, 3)
        expected_moves = set([
            # Northwest diagonal (including capture)
            (2, 2), (1, 1),
            # Northeast diagonal
            (2, 4), (1, 5), (0, 6),
            # Southwest diagonal
            (4, 2), (5, 1), (6, 0),
            # Southeast diagonal (including capture)
            (4, 4), (5, 5)
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_pawn_basic_movement_white(self):
        # Place a white pawn in starting position
        self.board.field[6][3].piece = Piece('p', 'white')
        valid_moves = self.white_agent.check_moves(6, 3)
        
        # Pawn should be able to move one or two squares forward from starting position
        expected_moves = set([
            (5, 3),  # One square forward
            (4, 3)   # Two squares forward
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_pawn_basic_movement_black(self):
        # Place a black pawn in starting position
        self.board.field[1][3].piece = Piece('p', 'black')
        valid_moves = self.black_agent.check_moves(1, 3)
        
        # Pawn should be able to move one or two squares forward from starting position
        expected_moves = set([
            (2, 3),  # One square forward
            (3, 3)   # Two squares forward
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_pawn_blocked_movement(self):
        # Place a white pawn with pieces blocking its path
        self.board.field[6][3].piece = Piece('p', 'white')
        self.board.field[5][3].piece = Piece('p', 'black')  # Blocking piece one square ahead
        
        valid_moves = self.white_agent.check_moves(6, 3)
        expected_moves = set()  # No valid moves when blocked
        self.assertEqual(set(valid_moves), expected_moves)

    def test_pawn_diagonal_capture(self):
        # Place a white pawn with enemy pieces in capture positions
        self.board.field[6][3].piece = Piece('p', 'white')
        self.board.field[5][2].piece = Piece('p', 'black')  # Enemy piece diagonal left
        self.board.field[5][4].piece = Piece('p', 'black')  # Enemy piece diagonal right
        
        valid_moves = self.white_agent.check_moves(6, 3)
        expected_moves = set([
            (5, 2),  # Capture left
            (5, 3),  # Forward one
            (5, 4),  # Capture right
            (4, 3)   # Forward two (from starting position)
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_knight_basic_movement(self):
        # Place a white knight in the middle of an empty board
        self.board.field[3][3].piece = Piece('n', 'white')
        valid_moves = self.white_agent.check_moves(3, 3)
        
        # Knight should be able to move in L-shapes in all eight possible positions
        expected_moves = set([
            (1, 2), (1, 4),  # Up 2, left/right 1
            (2, 1), (2, 5),  # Up 1, left/right 2
            (4, 1), (4, 5),  # Down 1, left/right 2
            (5, 2), (5, 4)   # Down 2, left/right 1
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_knight_edge_of_board(self):
        # Place a white knight near the edge of the board
        self.board.field[0][0].piece = Piece('n', 'white')
        valid_moves = self.white_agent.check_moves(0, 0)
        
        # Knight should only have valid moves within the board
        expected_moves = set([
            (1, 2),  # Down 1, right 2
            (2, 1)   # Down 2, right 1
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_knight_capture_and_friendly_blocking(self):
        # Place a white knight with both friendly and enemy pieces
        self.board.field[3][3].piece = Piece('n', 'white')
        self.board.field[1][2].piece = Piece('p', 'white')  # Friendly piece blocking
        self.board.field[1][4].piece = Piece('p', 'black')  # Enemy piece to capture
        
        valid_moves = self.white_agent.check_moves(3, 3)
        expected_moves = set([
            (1, 4),  # Capture enemy piece
            (2, 1), (2, 5),  # Up 1, left/right 2
            (4, 1), (4, 5),  # Down 1, left/right 2
            (5, 2), (5, 4)   # Down 2, left/right 1
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_king_basic_movement(self):
        # Place a white king in the middle of an empty board
        self.board.field[3][3].piece = Piece('k', 'white')
        valid_moves = self.white_agent.check_moves(3, 3)
        
        # King should be able to move one square in any direction
        expected_moves = set([
            (2, 2), (2, 3), (2, 4),    # All squares in the row above
            (3, 2), (3, 4),            # Left and right squares
            (4, 2), (4, 3), (4, 4)     # All squares in the row below
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_king_edge_of_board(self):
        # Place a white king at the edge of the board
        self.board.field[0][0].piece = Piece('k', 'white')
        valid_moves = self.white_agent.check_moves(0, 0)
        
        # King should only have valid moves within the board
        expected_moves = set([
            (0, 1),  # Right
            (1, 0),  # Down
            (1, 1)   # Down-right
        ])
        self.assertEqual(set(valid_moves), expected_moves)

    def test_king_capture_and_friendly_blocking(self):
        # Place a white king with both friendly and enemy pieces
        self.board.field[3][3].piece = Piece('k', 'white')
        self.board.field[2][2].piece = Piece('p', 'white')  # Friendly piece blocking
        self.board.field[2][3].piece = Piece('p', 'black')  # Enemy piece to capture
        
        valid_moves = self.white_agent.check_moves(3, 3)
        expected_moves = set([
            (2, 3),  # Capture enemy piece
            (2, 4),  # Up-right
            (3, 2), (3, 4),  # Left and right
            (4, 2), (4, 3), (4, 4)  # All squares in the row below
        ])
        self.assertEqual(set(valid_moves), expected_moves)

if __name__ == '__main__':
    unittest.main() 