
class TicTacToe():

    def __init__(self , state = ['_' for _ in range(9)] , turn = 'x'):
        self.state = state
        self.winner = None
        self.turn = turn
        self.isRunning = True

    def getCurrentTurn(self):
        return self.turn

    def getWinner(self):
        return self.winner

    def isTerminal(self):
        count = 0
        for i in self.state:
            if i == '_' :
                count += 1
        return count == 0

    def checkGameOver(self):
        
        rowx = [0 , 0 , 0]
        colx = [0 , 0 , 0]
        
        rowo = [0 , 0 , 0]
        colo = [0 , 0 , 0]

        for i , player in enumerate(self.state):
            if player == 'x' :
                rowx[i//3] +=1
                colx[i%3] +=1
            elif player == 'o':
                rowo[i//3] +=1
                colo[i%3] +=1

        for i in range(3):
            if (rowx[i] == 3 or colx[i] == 3):
                self.winner = 'x'
                self.isRunning = False
                return True
            
            if (rowo[i] == 3 or colo[i] == 3):
                self.winner = 'o'
                self.isRunning = False
                return True

        if self.state[4] != '_' and ((self.state[0] == self.state[4] and self.state[4] == self.state[8])
                                      or (self.state[2] == self.state[4] and self.state[4] == self.state[6])):
            self.winner = self.state[4]
            self.isRunning = False
            return True


        if self.isTerminal():
            self.winner = 'draw'
            self.isRunning = False
            return True

        return False

    @staticmethod
    def generateMove(state , turn ,  index):
        if state[index] == '_':
            state[index] = turn  
            return state
        return None

    def generateNextStates(self):
        states = []
        for i , player in enumerate(self.state):
            if player != '_' : continue
            newState = self.generateMove(self.state , self.turn , i)
            states.append(newState)
        return states

    def makeMove(self , row , col):
        index = row*3 + col
        state = self.generateMove(self.state , self.turn , index)
        if state is not None:
            self.state = state
            self.turn = 'x' if self.turn == 'o' else 'o'
            return True
        return False

    def makeMove(self , state):
        self.state = state
        self.turn = 'x' if self.turn == 'o' else 'o'

    def utility(self , player):
        if not self.checkGameOver():
            return None

        if self.winner == "draw":
            return 0
        
        if player == self.winner :
            return 1
        else:
            return -1