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

    def move(self,start_coordinate,end_coordinate):
        piece = self.board[start_coordinate[0]][start_coordinate[1]]
        if self.white_to_move and piece[0] == "w":
            self.board[start_coordinate[0]][start_coordinate[1]] = "--"
            self.board[end_coordinate[0]][end_coordinate[1]] = piece
        else:
            print("Cant move black piece")


