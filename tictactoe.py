
class TicTacToe():

    def __init__(self , state = None , turn = 'x'):
        if state is None :
            self.state = ['_']*9
        else:
            self.state = state.copy()
        self.winner = None
        self.turn = turn
        self.isRunning = True

    def getCurrentTurn(self):
        return self.turn

    def getWinner(self):
        return self.winner

    def isTerminal(self , state:list):
        
        count = 0
        for i in state:
            if i == '_' :
                count += 1
        return count == 0

    def checkGameOverState(self , state:list):
            
            rowx = [0 , 0 , 0]
            colx = [0 , 0 , 0]
            
            rowo = [0 , 0 , 0]
            colo = [0 , 0 , 0]
    
            for i , player in enumerate(state):
                if player == 'x' :
                    rowx[i//3] +=1
                    colx[i%3] +=1
                elif player == 'o':
                    rowo[i//3] +=1
                    colo[i%3] +=1
    
            for i in range(3):
                if (rowx[i] == 3 or colx[i] == 3):
                    return True , 'x'
                
                if (rowo[i] == 3 or colo[i] == 3):
                    return True , 'o'
    
            if state[4] != '_' and ((state[0] == state[4] and state[4] == state[8])
                                          or (state[2] == state[4] and state[4] == state[6])):
                return True , state[4]
    
    
            if self.isTerminal(state):
                return True , 'draw'
    
            return False , None

    def generateMove(self , state:list , turn ,  index):
        if index < 0 or index >= 9 :
            return None
        newState = state.copy()
        if newState[index] == '_':
            newState[index] = turn  
            return newState
        return None

    def generateNextStates(self , state , turn):
        if self.checkGameOverState(state)[0]:
            return []
        states = []
        for i , player in enumerate(state):
            if player != '_' : continue
            newState = self.generateMove(state , turn , i)
            states.append(newState)
        return states

    def makeMove(self , row , col):
        if not (0 <= row < 3 and 0 <= col < 3):
            return False
        if not self.isRunning:
            return False
        index = row*3 + col
        state = self.generateMove(self.state , self.turn , index)
        if state is not None:
            self.state = state
            self.turn = 'x' if self.turn == 'o' else 'o'
            done , winner = self.checkGameOverState(self.state)
            if done:
                self.isRunning = False
                self.winner = winner
            return True
        return False

    def makeMoveState(self , state):
        self.state = state
        self.turn = 'x' if self.turn == 'o' else 'o'

    def utility(self , player , state):
        done , winner = self.checkGameOverState(state)
        if not done : return None

        if winner == "draw":
            return 0
        
        if player == winner :
            return 1
        else:
            return -1