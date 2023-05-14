class ChessPiece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def __str__(self):
        return self.color + " " + self.__class__.__name__ #using this, I can directly put the object in the index of the board and it will print the name of the piece

    def move(self):
        pass #placeholder

    def availableMoves(self):
        pass

    def printAvailableMoves(self):
        pass

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
    
    def __init__(self, color, position):
        super().__init__(color, position)
        self.hasMoved = False
        self.validMoves = []


    def move(self):
        pass

    def availableMoves(self):
        self.validMoves = []
        if self.hasMoved == False:
            self.validMoves.append((self.position[0] + 2, self.position[1]))
            self.validMoves.append((self.position[0] + 1, self.position[1]))

        else:
            self.validMoves.append((self.position[0] + 1, self.position[1]))

        return self.validMoves

    def printAvailableMoves(self):
        print("Available moves: ")
        row_mapping = {7: "1", 6: "2", 5: "3", 4: "4", 3: "5", 2: "6", 1:"7", 0:"8"}
        column_mapping = {0: "A", 1: "B", 2: "C", 3: "D", 4:"E", 5:"F", 6:"G", 7:"H"}
        
        for move in self.validMoves:
            row = row_mapping[move[0]]
            column = column_mapping[move[1]]
            print(column + row)


        
            


    

        
    


