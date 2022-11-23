from piece import Piece

class Square:
    def __init__(self, new_x, new_y, new_piece = None):
        self.x = new_x
        self.y = new_y
        self.piece: Piece = new_piece

    def get_piece(self) -> Piece:
        return self.piece

    def __repr__(self):
        return "(%s, %s) %s" % (self.x,self.y,self.piece)