class GameState:
    def __init__(self):
        self.board = [["bR","bN","bB","bQ","bK","bB","bN","bR"],
                 ["bP","bP","bP","bP","bP","bP","bP","bP"],
                 ["--","--","--","--","--","--","--","--"],
                 ["--","--","--","--","--","--","--","--"],
                 ["--","--","--","--","--","--","--","--"],
                 ["--","--","--","--","--","--","--","--"],
                 ["wp","wp","wp","wp","wp","wp","wp","wp"],
                 ["wr","wn","wb","wq","wk","wb","wn","wr"],]
        self.move_log = []
        self.white_to_move = True

def move()