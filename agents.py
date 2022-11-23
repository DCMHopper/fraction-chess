from board import Board

class GenericAgent:
    def __init__(self, board: Board, color):
        self.board: Board = board
        self.color = color

    def check_moves(self,x,y):
        cur_square = self.board.field[x][y]
        if cur_square.piece.rank is 'r':
            return self.ortho_scan(x, y, cur_square)
        if cur_square.piece.rank is 'b':
            valid = []
            x_scan = x
            y_scan = y
            while x_scan>0 and y_scan>0:
                x_scan-=1
                y_scan-=1
                frontier = self.board.field[x_scan][y_scan]
                if frontier.piece is not None and frontier.piece.color == cur_square.piece.color:
                    break
                valid.append((x_scan,y_scan))
                if frontier.piece is not None and frontier.piece.color != cur_square.piece.color:
                    break

    def ortho_scan(self, x, y, cur_square):
        valid = []
        x_scan = x
        while x_scan > 0:
            x_scan-=1
            frontier = self.board.field[x_scan][y]
            if frontier.piece is not None and frontier.piece.color == cur_square.piece.color:
                break
            valid.append((x_scan,y))
            if frontier.piece is not None and frontier.piece.color != cur_square.piece.color:
                break
        x_scan = x
        while x_scan < self.board.size-1:
            x_scan+=1
            frontier = self.board.field[x_scan][y]
            if frontier.piece is not None and frontier.piece.color == cur_square.piece.color:
                break
            valid.append((x_scan,y))
            if frontier.piece is not None and frontier.piece.color != cur_square.piece.color:
                break
        y_scan = y
        while y_scan > 0:
            y_scan-=1
            frontier = self.board.field[x][y_scan]
            if frontier.piece is not None and frontier.piece.color == cur_square.piece.color:
                break
            valid.append((x,y_scan))
            if frontier.piece is not None and frontier.piece.color != cur_square.piece.color:
                break
        y_scan = y
        while y_scan < self.board.size-1:
            y_scan+=1
            frontier = self.board.field[x][y_scan]
            if frontier.piece is not None and frontier.piece.color == cur_square.piece.color:
                break
            valid.append((x,y_scan))
            if frontier.piece is not None and frontier.piece.color != cur_square.piece.color:
                break
        return valid
