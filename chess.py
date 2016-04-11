class Player:
    def __init__(self,player):
        self.name=""
        self.naming(player)

    def printName(self):
        print(self.name)

    def get(self):
        return self.name
    def naming(self,player):
        while(True):
            name=input("Input Player ("+player+"):")
            if name!="":
                self.name=name
                print("Player",player,"Name:",self.name,"\n")
                break
            else:
                print("\nName can not be empty!")

class Chess:
    def __init__(self,rank,color,x,y):
        self.rank=rank
        self.color=color
        self.jump=False
        self.swim=False
        self.x = x
        self.y = y
    def getRank(self):
        return self.rank
    def getPosition(self):
        return self.x,self.y
    def updatePos(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return self.color+str(self.rank)
class Board:
    def __init__(self):
        self.board=[]
        for row in range(9): self.board+=[['']*7]
        self.chessBoard=[]
        for row in range(9): self.chessBoard+=[['']*7]
    def start(self):
        self.board[0][2]="#"
        self.board[0][4]="#"
        self.board[1][3]="#"
        self.board[8][2]="#"
        self.board[8][4]="#"
        self.board[7][3]="#"
        self.board[0][3]="@"
        self.board[8][3]="@"
        for i in range(3,6):
            for j in range(1,3):
                self.board[i][j]="~~"
            for j in range(4,6):
                self.board[i][j]="~~"
        self.chessBoard[0][0]=Chess(6,"A",0,0)#Lion
        self.chessBoard[0][6]=Chess(5,"A",0,6)#Tiger
        self.chessBoard[1][1]=Chess(2,"A",1,1)#Dog
        self.chessBoard[1][5]=Chess(1,"A",1,5)#Cat
        self.chessBoard[2][0]=Chess(0,"A",2,0)#Rat
        self.chessBoard[2][2]=Chess(4,"A",2,2)#Leopard
        self.chessBoard[2][4]=Chess(3,"A",2,4)#Wolf
        self.chessBoard[2][6]=Chess(8,"A",2,6)#Elephant
        self.chessBoard[8][6]=Chess(6,"B",8,6)#Lion
        self.chessBoard[8][0]=Chess(5,"B",8,0)#Tiger
        self.chessBoard[7][5]=Chess(2,"B",7,5)#Dog
        self.chessBoard[7][1]=Chess(1,"B",7,1)#Cat
        self.chessBoard[6][6]=Chess(0,"B",6,6)#Rat
        self.chessBoard[6][4]=Chess(4,"B",6,4)#Leopard
        self.chessBoard[6][2]=Chess(3,"B",6,2)#Wolf
        self.chessBoard[6][0]=Chess(8,"B",6,0)#Elephant
        
    def printRank(self):
        pieces=["Rat","Cat","Dog","Wolf","Leopard","Tiger","Lion","Elephant"]
        print("\n+","-"*9,"+","-"*9,"+",sep="")
        print("|","%8s "%"Rank","|","%8s "%"Piece","|",sep="")
        print("+","-"*9,"+","-"*9,"+",sep="")
        i=0
        for i in range(0,len(pieces)):
            print("|","%8s "%i,"|","%8s "%pieces[i],"|",sep="")
            print("+","-"*9,"+","-"*9,"+",sep="")
            
    def printBoard(self):
        self.printRank()
        print("\n--|+-----+-----+-----+-----+-----+-----+-----+")
        print("--|",sep="",end="")
        for x in range(0,7):
            print("|%5s"%chr(65+x),sep="",end="")
        print("|\n--|+-----+-----+-----+-----+-----+-----+-----+")
        for i in range(0,9):
            print("%2d|"%i,sep="",end="")
            for j in range(0,7):
                print("|%4s "%(str(self.chessBoard[i][j])+self.board[i][j]),sep="",end="")
            print("|\n--|+-----+-----+-----+-----+-----+-----+-----+")
    def updatePosition(self,chess,x,y):
        chess.updatePos(x,y)
        self.chessBoard[x][y]=chess
        
    def getPosition(self):
        return self.chessBoard[x][y]

    def getSpecialGrid(self, x, y):
        return self.board[x][y]
    
class Game:
    def __init__(self):
        self.running=False
        self.playerA=None
        self.playerB=None
        self.board=None
        self.gameStart()
        self.turnA=True
        
    def initVar(self):
        self.running=True
        self.playerA=Player("A")
        self.playerB=Player("B")
        self.board=Board()
        self.board.start()
    def gameStart(self):
        self.initVar()
        while(self.running):
            self.board.printBoard()
            move=input()
            #break
            
            
    def endGame(self):
        print("Game Ended!")
        if(self.askReplay()):
            self.initVar()

    def askReplay(self):
        replay=input("Do you want to play again?(Yes/No):")
        replay=replay[:1].lower
        play=False
        if replay=="y":
            play=True
        return play


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
    #returns "end" if someone won
    #returns false otherwised
    
    def validateMove(chessA, x, y, board):
        if board.getSpecialGrid(x, y) == "@":
            if validateWin(chessA, x, y, board) == True:
                return "end"
        if board.getSpecialGrid(x, y) == "#":
            return validateTrap(chessA, x, y, board)
        if chessA.swim == True and board.getSpecialGrid(x, y) == "water":
            return validateSwim(chessA, x, y, board)
        if chessA.jump == True and board.getSpecialGrid(x, y) == "water":
            return validateJump(chessA, x, y, board)
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


    def validateSwim(chessA, x, y, board):
        Ax, Ay = chessA.getPostion()
        chessB = board.getPosition(x,y)
        if chessB == 0:
            if abs(Ax-x) == 1 and abs(Ay-y) == 1:
                board.updatePosition(chessA, x, y)
                return True
        else:
            return False
    
    def validateJump(chessA, x, y, board):
        count = 0
        Ax, Ay = chessA.getPostion()
        if abs(Ax-x) == 1 and abs(Ay-y) == 1:
            for i in range(x,x+3):
                count = 0
                for j in range(y,y+3):
                    if board.getSpecialGrid(i, j) == "~~" :
                        if not(board.getPosition(i,j) == 0) and board.getPosition(i,j).rank == 0:
                            break
                        count = count+1
                    elif count == 2 or count == 3:
                        return validateMove(chessA, i, j, board)

            for j in range(y,y+3):
                count = 0
                for i in range(x,x+3):
                    if board.getSpecialGrid(i, j) == "~~" :
                        if not(board.getPosition(i,j) == 0) and board.getPosition(i,j).rank == 0:
                            break
                        count = count+1
                    elif count == 2 or count == 3:
                        return validateMove(chessA, i, j, board)
        return False


    def validateWin(chessA, x, y, board):
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

    def validateTrap(chessA, x, y, board):
        Ax, Ay = chessA.getPostion()
        if abs(Ax-x) == 1 and abs(Ay-y) == 1:
            board.updatePosition(chessA, x, y)
            return True
        return False
    
if __name__=="__main__":
    Game()
