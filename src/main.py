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
      player = reinforcement.Player(value)
      num_games = int(raw_input('Number of training games: '))
      player.train(num_games)
      return player


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
    action = player.getAction(board)

    board.playAction(action, value)

    if board.isWinner(value):
      break
    elif not board.getAllowedActions():
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
