from board import Board
import human
import minimax

def main():
  board = Board()

  player_x = human.Player()
  player_o = minimax.Player()
  x_turn = True

  # Game loop.
  while True:
    value = Board.X if x_turn else Board.O

    print('\n%s' % board)
    print('\nPlayer %s' % value)

    player = player_x if x_turn else player_o
    r, c = player.getMove(board, value)

    board.setCell(r, c, value)

    if board.isWinner(value):
      break
    elif not board.getEmptyCells():
      value = Board.EMPTY
      break

    x_turn = not x_turn

  # Game over.
  if value == Board.EMPTY:
    print('\nDraw\n')
  else:
    print('\nPlayer %s wins!\n' % value)

  print(board)


if __name__ == '__main__':
  main()
