from ChessBoard import ChessBoard

def Main():
    print ("Welcome to ChessAI! A game I just happened to develop in my spare time.")
    chessBoard = ChessBoard()
    chessBoard.initialSetup()
    chessBoard.printBoard()

if __name__ == "__main__":
    Main()

