import copy
import random

from board import Board


class Player(object):

  def __init__(self, value):
    self._value = value
    self._cache = {}

  def getAction(self, board):
    score, actions = self._minimax(board, self._value)
    return actions[random.randrange(len(actions))]

  def _minimax(self, board, value):
    state = hash(board)
    if state in self._cache:
      return self._cache[state]

    actions = board.getAllowedActions()
    if not actions:
      return 0, (None, None)  # Draw.

    best_score = -1
    best_actions = []

    for action in actions:
      board_copy = copy.deepcopy(board)
      board_copy.playAction(action, value)

      if board_copy.isWinner(value):
        score = 1  # Win.
      else:
        result = self._minimax(board_copy, Board.X if value == Board.O else Board.O)
        score = -result[0]

      if score > best_score:
        best_score = score
        best_actions = [action]
      elif score == best_score:
        best_actions.append(action)

    result = self._cache[state] = (best_score, best_actions)
    return result
