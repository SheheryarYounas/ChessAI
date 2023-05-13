class ChessPiece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def __str__(self):
        return self.color + " " + self.__class__.__name__ #using this, I can directly put the object in the index of the board and it will print the name of the piece

    def move(self):
        pass #placeholder

class King(ChessPiece):
    def move(self):
        pass

class Queen(ChessPiece):
    def move(self):
        pass

class Rook(ChessPiece):
    def move(self):
        pass

class Bishop(ChessPiece):
    def move(self):
        pass

class Knight(ChessPiece):
    def move(self):
        pass

class Pawn(ChessPiece):
    def move(self):
        pass


