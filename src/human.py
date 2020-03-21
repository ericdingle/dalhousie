class Player(object):

  def getMove(self, board, value):
    r = raw_input("Row: ")
    c = raw_input("Column: ")
    return (int(r), int(c))
