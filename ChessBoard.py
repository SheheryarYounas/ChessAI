from ChessPiece import King, Queen, Rook, Bishop, Knight, Pawn

class ChessBoard:
    def __init__(self):
        self.board = [["-" for _ in range(8)] for _ in range(8)]
        self.validMoves = []

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
        print("           A              B             C               D             E              F             G                 H")
        for i, row in enumerate(self.board):
            rowString = [str(piece) if piece else '-' for piece in row]
            print(str(8 - i) + "   " + str(rowString))

    def checkPositionForPiece(self, position):
        if self.board[position[0]][position[1]] == "-":
            return False
        else:
            return True
    
    def selectPiece(self):
        print("Select a piece to move (Example: A1): ")
        positionInput = input()

        column_mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G":6, "H":7}
        row_mapping = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7":1, "8":0}

        try:
            column = column_mapping[positionInput[0].upper()]
            row = row_mapping[positionInput[1]]

            if self.checkPositionForPiece((row, column)) and self.board[row][column].color == "White":
                print("You have selected a " + str(self.board[row][column]))
            
            else:
                print("There is no piece at that position or you have selected the opponent's piece. Please try again.")
                self.selectPiece()            
                        
        except KeyError: #KeyError will occur if an input outside the mapping is given.
            print("The position you have entered is invalid. Please try again.")
            self.selectPiece()
        
        self.availableMoves(self.board[row][column])

    def availableMoves(self, piece):
        self.validMoves = piece.availableMoves()
        piece.printAvailableMoves()
        recursion_elimination = 0
        
        column_mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G":6, "H":7}
        row_mapping = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7":1, "8":0}

        print("Select a position to move to (Example: A1): ")
        positionInput = input()

        try:
            row = row_mapping[positionInput[1]]
            column = column_mapping[positionInput[0].upper()]
            if (int(row), int(column)) in self.validMoves:
                self.board[piece.position[0]][piece.position[1]] = "-"
                self.board[int(row)][int(column)] = piece
                piece.position = (int(row), int(column))
                recursion_elimination = 0

                if (isinstance(piece, Pawn)):
                    piece.hasMoved = True

            else:
                print("The position you have entered is not a valid move. Please try again.")
                recursion_elimination = 1
                self.availableMoves(piece)
        
        except KeyError:
            print("The position you have entered is invalid. Please try again.")
            self.availableMoves(piece)
        
        if recursion_elimination == 0:
            self.printBoard()





        






        
        




    

