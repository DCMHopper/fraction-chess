class Piece:
    def __init__(self, new_rank, new_color):
        self.rank = new_rank 
        self.color = new_color 
    
    def __repr__(self):
        return "[%s %s]" % (self.color, self.rank)
