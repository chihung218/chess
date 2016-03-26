class Player:
    def __init__(self,name):
        self.name=name

    def printName(self):
        print(self.name)

    def get(self):
        return self.name
    def rename(self):
        while(True):
            name=input("Input new name (",self.name," ):",sep="",end="")
            if name!="":
                self.name=name
                break
            else:
                print("Name can not be empty!")

class Chess:
    pieces={"Rat","Cat","Dog","Wolf","Leopard","Tiger","Lion","Elephant"}
    def __init__(self,rank,color,x,y):
        self.rank=rank
        self.color=color
        self.piece=pieces[sel.rank]
        self.jump=False
        self.swim=False
        self.x = x
        self.y = y
    def getRank(self):
        return self.rank
    def getPosition(self):
        return self.x,self.y

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

    def endGame(self,winner):
        if(self.running ):#& ((self.getPlayer(winner)==self.playerA)|(self.getPlayer(winner)==self.playerB))):
            self.running=False
            self.winner=winner
            print(self.winner,"is the winner!!")
            self.askReplay()
        else:
            print("Game Cannot End")
    def askReplay(self):
        replay=input("Do you want to play again?(Yes/No):")


class Rules():
    
    #input: 2 chess pieces
    #checks if chess A can eat chess B based on ranks, return true if A can eat B
    #returns false otherwise
    
    def validateEat(chessA, chessB):
        if chessA.getRank() == 0 and chessB.getRank() == 7:
            return True
        if chessA.getRank() == 7 and chessB.getRank() == 0:
            return False
        if chessA.getRank() >= chessB.getRank():
            return True
        else:
            return False

    #input:
    #Chess: the piece that wants to move
    #int: x position of location
    #int: y position of target
    #board: the board that the chess piece is moving on
    #returns true if the movement follows the rules of the game
    #returns false otherwised
    
    def validateMove(chessA, x, y, board):
        Ax, Ay = chessA.getPostion()
        chessB = board.getPosition(x,y)
        if chessB == 0:
            if abs(Ax-x) == 1 and abs(Ay-y) == 1:
                board.updatePosition(chessA, x, y)
                return True
        elif validateEat(chessA, chessB):
            board.updatePosition(chessA, x, y)
            return True
        return False


def main():
    g=Game()
    g.gameStart()
    g.endGame("")

if __name__=="__main__":
    main()
