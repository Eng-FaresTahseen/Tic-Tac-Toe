
class Ai():

    def __init__(self , player , game):
        self.player = player
        self.opponent = 'x' if player == 'o' else 'o'
        self.game = game

    def _min(self , state , alpha , beta):
        done , winner = self.game.checkGameOverState(state)
        if done:
            return self.game.utility(self.player , state)

        val = float('inf')
        for child in self.game.generateNextStates(state , self.opponent):
            val = min(self._max(child , alpha , beta ) , val)
            beta = min(beta , val)
            if alpha >= beta :
                break

        return val

    def _max(self, state , alpha , beta):
        done , winner = self.game.checkGameOverState(state)
        if done:
            return self.game.utility( self.player , state)

        val = float('-inf')
        for child in self.game.generateNextStates(state , self.player):
            val = max(self._min(child , alpha , beta ) , val)
            alpha = max(alpha , val)
            if alpha >= beta :
                break

        return val

    def _minMax(self):

        done , winner = self.game.checkGameOverState(self.game.state)
        if done:
            return None

        if self.game.turn != self.player:
            raise RuntimeError("It's not the AI's turn to play.")

        bestVal = float('-inf')
        bestIndex = None

        alpha = float('-inf') 
        beta = float('inf')

        for index , cell in enumerate(self.game.state):
            if cell != '_':
                continue
            child = self.game.generateMove(self.game.state , self.player , index)
            val = self._min(child , alpha , beta)
            if val > bestVal:
                bestVal = val
                bestIndex = index

            alpha = max(alpha , bestVal)

        return bestIndex

    def makeTurn(self):
        index = self._minMax()
        if index is not None:
            self.game.makeMove(index // 3, index % 3)
            return True
        return False

