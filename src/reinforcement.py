from collections import defaultdict
import random

from board import Board
import minimax

class Player(object):

  ALPHA = 0.1

  def __init__(self, value):
    self._value = value
    self._policy = defaultdict(lambda: defaultdict(lambda: 0.5))

  def train(self, num_games):
    value = Board.X if self._value == Board.O else Board.O
    opponent = minimax.Player(value)

    for i in range(num_games):
      percent = 100.0 * i / num_games
      if percent % 10 == 0:
        print('%d%%' % percent)

      board = Board()

      if value == Board.X:  # X plays first.
        board.playAction(opponent.getAction(board), value)

      game_over = False
      while not game_over:
        state = hash(board)  # Store this before any actions are played.

        action = self.getAction(board, epsilon=0.2)
        board.playAction(action, self._value)

        game_over = True
        if board.isWinner(self._value):
          reward = 1.0  # Win.
        elif not board.getAllowedActions():
          reward = 0.5  # Draw.
        else:
          board.playAction(opponent.getAction(board), value)
          if board.isWinner(value):
            reward = 0.0  # Lose.
          elif not board.getAllowedActions():
            reward = 0.5  # Draw.
          else:
            game_over = False
            actions = board.getAllowedActions()
            reward = max(self._policy[hash(board)][action] for action in actions)

        self._policy[state][action] += self.ALPHA * (reward - self._policy[state][action])

  def getAction(self, board, epsilon=0.0):
    actions = board.getAllowedActions()

    if epsilon and random.random() < epsilon:
      return actions[random.randrange(len(actions))]

    state = hash(board)
    best_score, best_action = 0, None

    for action in actions:
      score = self._policy[state][action]
      if score > best_score:
        best_score, best_action = score, action

    return best_action
