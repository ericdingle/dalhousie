class Player(object):

  def getAction(self, board):
    r = raw_input("Row: ")
    c = raw_input("Column: ")
    return (int(r), int(c))
