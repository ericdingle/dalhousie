from collections import defaultdict
import minimax

class Player(object):

  def __init__(self, value):
    self._value = value
    self._policy = defaultdict(lambda: defaultdict(lambda: 0.5))

  def getMove(self, board):
    state = hash(board)
    moves = board.getEmptyCells()

    best_score = 0
    best_move = None
    for move in moves:
      score = self._policy[hash][move]
      if score > best_score:
        best_score = score
        best_move = move

    return best_move
