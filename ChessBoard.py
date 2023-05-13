from ChessPiece import King, Queen, Rook, Bishop, Knight, Pawn

class ChessBoard:
    def __init__(self):
        self.board = [["-" for _ in range(8)] for _ in range(8)]

    def initialSetup(self):
        #Placing white pieces
        self.board[0][0] = Rook("White", (0, 0))
        self.board[0][1] = Knight("White", (0, 1))
        self.board[0][2] = Bishop("White", (0, 2))
        self.board[0][3] = Queen("White", (0, 3))
        self.board[0][4] = King("White", (0, 4))
        self.board[0][5] = Bishop("White", (0, 5))
        self.board[0][6] = Knight("White", (0, 6))
        self.board[0][7] = Rook("White", (0, 7))
        for i in range(8):
            self.board[1][i] = Pawn("White", (1, i))
        
        #Placing black pieces
        self.board[7][0] = Rook("Black", (7, 0))
        self.board[7][1] = Knight("Black", (7, 1))
        self.board[7][2] = Bishop("Black", (7, 2))
        self.board[7][3] = Queen("Black", (7, 3))
        self.board[7][4] = King("Black", (7, 4))
        self.board[7][5] = Bishop("Black", (7, 5))
        self.board[7][6] = Knight("Black", (7, 6))
        self.board[7][7] = Rook("Black", (7, 7))
        for i in range(8):
            self.board[6][i] = Pawn("Black", (6, i))

    def printBoard(self):
        for row in self.board:
            rowString = [str(piece) if piece else '-' for piece in row]
            print(rowString)
    

