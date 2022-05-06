class Board:
    def __init__(self):
        self.field = []
        for i in range(8):
            tmp_row = []
            for j in range(8):
                if i == 0:
                    if j in [0,7]:
                        tmp_piece = Piece('r','w')
                        tmp_row.append(Square(i,j,tmp_piece))
                    elif j in [1,6]:
                        tmp_piece = Piece('n','w')
                        tmp_row.append(Square(i,j,tmp_piece))
                    elif j in [2,5]:
                        tmp_piece = Piece('b','w')
                        tmp_row.append(Square(i,j,tmp_piece))
                    elif j in [3]:
                        tmp_piece = Piece('q','w')
                        tmp_row.append(Square(i,j,tmp_piece))
                    elif j in [4]:
                        tmp_piece = Piece('k','w')
                        tmp_row.append(Square(i,j,tmp_piece))
                    else:
                        tmp_row.append(Square(i,j))
                elif i == 1:
                    tmp_piece = Piece('p','w')
                    tmp_row.append(Square(i,j,tmp_piece))
                elif i == 3 and j == 3:
                    tmp_piece = Piece('r','w')
                    tmp_row.append(Square(i,j,tmp_piece))
                elif i == 6:
                    tmp_piece = Piece('p','b')
                    tmp_row.append(Square(i,j,tmp_piece))
                elif i == 7:
                    if j in [0,7]:
                        tmp_piece = Piece('r','b')
                        tmp_row.append(Square(i,j,tmp_piece))
                    elif j in [1,6]:
                        tmp_piece = Piece('n','b')
                        tmp_row.append(Square(i,j,tmp_piece))
                    elif j in [2,5]:
                        tmp_piece = Piece('b','b')
                        tmp_row.append(Square(i,j,tmp_piece))
                    elif j in [3]:
                        tmp_piece = Piece('q','b')
                        tmp_row.append(Square(i,j,tmp_piece))
                    elif j in [4]:
                        tmp_piece = Piece('k','b')
                        tmp_row.append(Square(i,j,tmp_piece))
                    else:
                        tmp_row.append(Square(i,j))
                else:
                    tmp_row.append(Square(i,j))
            self.field.append(tmp_row)

    def check_moves(self,x,y):
        cur_square = self.field[x][y]
        if cur_square.piece.rank is 'r':
            return self.ortho_scan(x, y, cur_square)
        if cur_square.piece.rank is 'b':
            valid = []
            x_scan = x
            y_scan = y
            while x_scan>0 and y_scan>0:
                x_scan-=1
                y_scan-=1
                frontier = self-field[x_scan][y_scan]
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
            frontier = self.field[x_scan][y]
            if frontier.piece is not None and frontier.piece.color == cur_square.piece.color:
                break
            valid.append((x_scan,y))
            if frontier.piece is not None and frontier.piece.color != cur_square.piece.color:
                break
        x_scan = x
        while x_scan < 7:
            x_scan+=1
            frontier = self.field[x_scan][y]
            if frontier.piece is not None and frontier.piece.color == cur_square.piece.color:
                break
            valid.append((x_scan,y))
            if frontier.piece is not None and frontier.piece.color != cur_square.piece.color:
                break
        y_scan = y
        while y_scan > 0:
            y_scan-=1
            frontier = self.field[x][y_scan]
            if frontier.piece is not None and frontier.piece.color == cur_square.piece.color:
                break
            valid.append((x,y_scan))
            if frontier.piece is not None and frontier.piece.color != cur_square.piece.color:
                break
        y_scan = y
        while y_scan < 7:
            y_scan+=1
            frontier = self.field[x][y_scan]
            if frontier.piece is not None and frontier.piece.color == cur_square.piece.color:
                break
            valid.append((x,y_scan))
            if frontier.piece is not None and frontier.piece.color != cur_square.piece.color:
                break
        return valid


class Square:
    def __init__(self, new_x, new_y, new_piece = None):
        self.x = new_x
        self.y = new_y
        self.piece = new_piece

    def get_piece(self):
        return self.piece

    def __repr__(self):
        return "(%s, %s) %s" % (self.x,self.y,self.piece)


class Piece:
    def __init__(self, new_rank, new_color):
        self.rank = new_rank 
        self.color = new_color 
    
    def __repr__(self):
        return "[%s %s]" % (self.color, self.rank)


board = Board()

print(board.field)

print(board.check_moves(3,3))