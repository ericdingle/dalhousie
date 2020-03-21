class Board(object):

  EMPTY = ' '
  X = 'X'
  O = 'O'

  def __init__(self):
    self._board = [[self.EMPTY for c in range(3)] for r in range(3)]

  def __hash__(self):
    rows = [''.join(columns) for columns in self._board]
    return hash(''.join(rows))

  def __str__(self):
    rows = ['|'.join(columns) for columns in self._board]
    return '\n-+-+-\n'.join(rows)

  def getEmptyCells(self):
    return [(r, c) for r in range(3) for c in range(3) if self._board[r][c] == self.EMPTY]

  def setCell(self, r, c, value):
    assert(self._board[r][c] == self.EMPTY)
    self._board[r][c] = value

  def isWinner(self, value):
    for r in range(3):
      if all([self._board[r][c] == value for c in range(3)]):
        return True
    for c in range(3):
      if all([self._board[r][c] == value for r in range(3)]):
        return True
    if all([self._board[x][x] == value for x in range(3)]):
      return True
    if all([self._board[x][2-x] == value for x in range(3)]):
      return True
    return False
