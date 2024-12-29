from board import Board

class GenericAgent:
    def __init__(self, board: Board, color):
        self.board: Board = board
        self.color = color

    def check_moves(self,x,y):
        cur_square = self.board.field[x][y]
        if cur_square.piece.rank == 'r':
            return self.ortho_scan(x, y, cur_square)
        if cur_square.piece.rank == 'b':
            return self.diag_scan(x, y, cur_square)
        if cur_square.piece.rank == 'p':
            return self.pawn_scan(x, y, cur_square)
        if cur_square.piece.rank == 'n':
            return self.knight_scan(x, y, cur_square)
        if cur_square.piece.rank == 'k':
            return self.king_scan(x, y, cur_square)
        return []

    def ortho_scan(self, x, y, cur_square):
        def scan_direction(start_x, start_y, dx, dy):
            valid = []
            curr_x, curr_y = start_x + dx, start_y + dy
            
            while (0 <= curr_x < self.board.size and 
                   0 <= curr_y < self.board.size):
                frontier = self.board.field[curr_x][curr_y]
                if frontier.piece is not None:
                    if frontier.piece.color == cur_square.piece.color:
                        break
                    valid.append((curr_x, curr_y))
                    break
                valid.append((curr_x, curr_y))
                curr_x, curr_y = curr_x + dx, curr_y + dy
            return valid

        # Scan in all four directions: left, right, up, down
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        valid_moves = []
        for dx, dy in directions:
            valid_moves.extend(scan_direction(x, y, dx, dy))
        
        return valid_moves

    def diag_scan(self, x, y, cur_square):
        def scan_direction(start_x, start_y, dx, dy):
            valid = []
            curr_x, curr_y = start_x + dx, start_y + dy
            
            while (0 <= curr_x < self.board.size and 
                   0 <= curr_y < self.board.size):
                frontier = self.board.field[curr_x][curr_y]
                if frontier.piece is not None:
                    if frontier.piece.color == cur_square.piece.color:
                        break
                    valid.append((curr_x, curr_y))
                    break
                valid.append((curr_x, curr_y))
                curr_x, curr_y = curr_x + dx, curr_y + dy
            return valid

        # Scan in all four diagonal directions: NW, NE, SW, SE
        directions = [(-1,-1), (-1,1), (1,-1), (1,1)]
        valid_moves = []
        for dx, dy in directions:
            valid_moves.extend(scan_direction(x, y, dx, dy))
        
        return valid_moves

    def pawn_scan(self, x, y, cur_square):
        valid_moves = []
        direction = -1 if cur_square.piece.color == 'white' else 1  # White moves up (-1), black moves down (+1)
        
        # Forward movement
        next_x = x + direction
        if 0 <= next_x < self.board.size:
            # Check one square forward
            if self.board.field[next_x][y].piece is None:
                valid_moves.append((next_x, y))
                
                # Check two squares forward if pawn hasn't moved (is in starting position)
                start_rank = 6 if cur_square.piece.color == 'white' else 1
                if x == start_rank:
                    two_forward = next_x + direction
                    if (0 <= two_forward < self.board.size and 
                        self.board.field[two_forward][y].piece is None):
                        valid_moves.append((two_forward, y))
        
        # Diagonal captures
        for dy in [-1, 1]:  # Check both left and right diagonals
            diag_x, diag_y = x + direction, y + dy
            if (0 <= diag_x < self.board.size and 
                0 <= diag_y < self.board.size):
                target_square = self.board.field[diag_x][diag_y]
                if (target_square.piece is not None and 
                    target_square.piece.color != cur_square.piece.color):
                    valid_moves.append((diag_x, diag_y))
        
        return valid_moves

    def knight_scan(self, x, y, cur_square):
        valid_moves = []
        # Generate knight moves dynamically:
        for primary in [1, 2]:
            secondary = 3 - primary
            for primary_sign in [-1, 1]:
                for secondary_sign in [-1, 1]:
                    moves = [
                        (primary * primary_sign, secondary * secondary_sign),
                        (secondary * secondary_sign, primary * primary_sign)
                    ]
                    
                    for dx, dy in moves:
                        new_x, new_y = x + dx, y + dy
                        # Check if move is within board bounds
                        if (0 <= new_x < self.board.size and 
                            0 <= new_y < self.board.size):
                            target_square = self.board.field[new_x][new_y]
                            # Square is empty or contains enemy piece
                            if (target_square.piece is None or 
                                target_square.piece.color != cur_square.piece.color):
                                valid_moves.append((new_x, new_y))
                    
        return valid_moves

    def king_scan(self, x, y, cur_square):
        valid_moves = []
        # Check all 8 squares around the king
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Skip the current position
                if dx == 0 and dy == 0:
                    continue
                    
                new_x, new_y = x + dx, y + dy
                # Check if move is within board bounds
                if (0 <= new_x < self.board.size and 
                    0 <= new_y < self.board.size):
                    target_square = self.board.field[new_x][new_y]
                    # Square is empty or contains enemy piece
                    if (target_square.piece is None or 
                        target_square.piece.color != cur_square.piece.color):
                        valid_moves.append((new_x, new_y))
        
        return valid_moves