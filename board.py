from square import Square
from piece import Piece

class Board:
    def __init__(self):
        self.size = 8
        self.field = []
        for i in range(self.size):
            tmp_row = []
            for j in range(self.size):
                tmp_piece = None
                if i == 0:
                    if j in [0,7]:
                        tmp_piece = Piece('r','w')
                    elif j in [1,6]:
                        tmp_piece = Piece('n','w')
                    elif j in [2,5]:
                        tmp_piece = Piece('b','w')
                    elif j in [3]:
                        tmp_piece = Piece('q','w')
                    elif j in [4]:
                        tmp_piece = Piece('k','w')
                elif i == 1:
                    tmp_piece = Piece('p','w')
                elif i == 3 and j == 3:
                    tmp_piece = Piece('r','w')
                elif i == 6:
                    tmp_piece = Piece('p','b')
                elif i == 7:
                    if j in [0,7]:
                        tmp_piece = Piece('r','b')
                    elif j in [1,6]:
                        tmp_piece = Piece('n','b')
                    elif j in [2,5]:
                        tmp_piece = Piece('b','b')
                    elif j in [3]:
                        tmp_piece = Piece('q','b')
                    elif j in [4]:
                        tmp_piece = Piece('k','b')
                
                tmp_row.append(Square(i,j,tmp_piece))

            self.field.append(tmp_row)

