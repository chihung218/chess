class Player:
    def __init__(self,name):
        self.name=name

    def printName(self):
        print(self.name)

    def get(self):
        return self.name

class Chess:
    pieces={"Rat","Cat","Dog","Wolf","Leopard","Tiger","Lion","Elephant"}
    def __init__(self,rank,color):
        self.rank=rank
        self.color=color
        self.piece=pieces[sel.rank]
        self.jump=False
        self.swim=False
    def getRank(self):
        return self.rank
class Board:
    def __init__(self):
        self.board=[[0]*7]*9
        self.chessBoard=[[0]*7]*9
    def start(self):
        for i in range(0,9):
            for j in range(0,7):
                self.chessBoard[i][j]=0               
    def printBoard(self):
        print("--|",sep="",end="")
        for x in range(0,7):
            print("|%3s"%chr(65+x),sep="",end="")
        print("|\n--|+---+---+---+---+---+---+---+")
        for i in range(0,9):
            print("%2d|"%i,sep="",end="")
            for j in range(0,7):
                print("|%3s"%self.chessBoard[i][j],sep="",end="")
            print("|\n--|+---+---+---+---+---+---+---+")
    def updatePosition(self,chess,x,y):
        self.chessBoard[x][y]=chess
        printBoard()
    def getPosition(self,x,y):
        return self.chessBoard[x][y]

    
class Game:
    def __init__(self):
        self.running=False
        self.playerA=None
        self.playerB=None
        self.winner=None
        self.board=None
    def gameStart(self):
        self.running=True
        self.playerA=Player("A")
        self.playerB=Player("B")
        self.board=Board()
        self.board.start()
        self.board.printBoard()
    def getPlayer(self,player):
        if player.upper=="A":
            return self.playerA
        elif player.upper=="B":
            return self.playerB
        else:
            #print("None such player")
            return None
    def endGame(self,winner=None):
        #print(winner)
        if (winner is None):
            raise TypeError("Invalid Input")
        #elif(self.running & ((self.getPlayer(winner)==self.playerA)|(self.getPlayer(winner)==self.playerB))):
#            self.running=False
#            self.winner=winner
        #else:
#            print("Game Cannot End")

    #def playerTurn(self):


class Rules():
    def validateEat(chessA, chessB):
        if chessA.getRank() == 0 and chessB.getRank() == 7:
            return True
        if chessA.getRank() == 7 and chessB.getRank() == 0:
            return False
        if chessA.getRank() >= chessB.getRank():
            return True
        else:
            return False

    #def validateMove(chessA, x, y, board):
        #if board.getPosition(x,y) == 0:
            

def main():
    g=Game()
    g.gameStart()
    g.endGame()

    
if __name__=="__main__":
    main()
