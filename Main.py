from ChessBoard import ChessBoard #from <file> import <class>

def Main():
    print ("Welcome to ChessAI! A game I just happened to develop in my spare time.")
    chessBoard = ChessBoard()
    chessBoard.initialSetup()
    chessBoard.printBoard()
    chessBoard.selectPiece()

if __name__ == "__main__":
    Main()

