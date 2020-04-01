class Player(object):

  def getMove(self, board):
    r = raw_input("Row: ")
    c = raw_input("Column: ")
    return (int(r), int(c))
