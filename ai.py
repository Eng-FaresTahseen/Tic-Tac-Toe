
class Ai():

    def __init__(self , player , game):
        self.player = player
        self.game = game
        self.candidateState = None

    def _min(self , state , alpha , beta):
        if self.checkGameOver(state):
            return self.game.utility(state , self.player)

        val = float('inf')
        for child in state.game.generateNextStates():
            val = min(self._max(self , child , alpha , beta ) , val)
            if alpha >= beta :
                break

    def _max(self, state , alpha , beta):
        if self.checkGameOver(state):
            return self.game.utility(state , self.player)

        val = float('-inf')
        for child in state.game.generateNextStates():
            candidate = max(self._min(self , child , alpha , beta ) , val)
            if candidate > val:
                self.candidateState = child
            val = candidate
            if alpha >= beta :
                break

    def _minMax(self):
        self._max(self.game.state , float('-inf') , float('inf'))

    def makeTurn(self):
        self._minMax(self)
        self.game.makeMove(self.candidateState)
