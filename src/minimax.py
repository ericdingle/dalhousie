import copy

from board import Board

class Player(object):

  def __init__(self, value):
    self._value = value

  def getMove(self, board):
    score, r, c = self._minimax(board, self._value)
    return (r, c)

  def _minimax(self, board, value):
    cells = board.getEmptyCells()
    if not cells:
      return 0, None, None

    max_score = -1
    row = column = None

    for (r, c) in board.getEmptyCells():
      board_copy = copy.deepcopy(board)
      board_copy.setCell(r, c, value)

      if board_copy.isWinner(value):
        score = 1
      else:
        result = self._minimax(board_copy, Board.X if value == Board.O else Board.O)
        score = -result[0]

      if score > max_score:
        max_score = score
        row = r
        column = c

    return (max_score, row, column)
