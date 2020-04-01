from board import Board
import human
import minimax
import reinforcement


def getPlayer(value):
  while True:
    a = raw_input('Player %s - 1) Human, 2) Minimax, 3) Reinforcement: ' % value)
    if a == '1':
      return human.Player()
    elif a == '2':
      return minimax.Player(value)
    elif a == '3':
      return reinforcement.Player(value)


def main():
  board = Board()

  player1 = getPlayer(Board.X)
  player2 = getPlayer(Board.O)
  turn = True  # True for player1 else False.

  # Game loop.
  while True:
    value = Board.X if turn else Board.O

    print('\n%s' % board)
    print('\nPlayer %s' % value)

    player = player1 if turn else player2
    r, c = player.getMove(board)

    board.setCell(r, c, value)

    if board.isWinner(value):
      break
    elif not board.getEmptyCells():
      value = Board.EMPTY
      break

    turn = not turn

  # Game over.
  if value == Board.EMPTY:
    print('\nDraw\n')
  else:
    print('\nPlayer %s wins!\n' % value)

  print(board)


if __name__ == '__main__':
  main()
