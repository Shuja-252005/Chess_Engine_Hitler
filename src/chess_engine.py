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

    def makeMove(self,move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.white_to_move = not self.white_to_move

    def undoMove(self):
        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move

    """Method for all moves with checks and stuff"""
    def getValidMoves(self):
        return self.getAllPossibleMoves()

    """All possible moves"""
    def getAllPossibleMoves(self):
        moves = [Move((7,7),(3,3),self.board)]
        for r in range(len(self.board)):
            for c in range((len(self.board[r]))):
                piece = self.board[r][c]
                if piece == "--":
                    continue
                color = piece[0]
                kind = piece[1]

                if (color == "w" and self.white_to_move) or (color == "b" and not self.white_to_move):
                    if kind == "p":
                        self.allPawnMoves(r,c,moves)
        return moves



    """All possible pawn moves"""
    def allPawnMoves(self,r,c,moves):
        pass



class Move:
    rowsToRank = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
    colsToFiles = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}


    def __init__(self,start_pos,end_pos,board):
        self.start_row = start_pos[0]
        self.start_col = start_pos[1]
        self.end_row = end_pos[0]
        self.end_col = end_pos[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

    """The chess notation is the notation for the complete move like (bp at a4 ---- wP at b3"""
    def getChessNotation(self):
        return self.getRankFile(self.start_row,self.start_col) +self.getRankFile(self.end_row,self.end_col)


    def getRankFile(self,r,c):
        return self.colsToFiles[c] + self.rowsToRank[r]

    def __eq__(self, other):
        if isinstance(other,Move):
            return (other.start_row == self.start_row and
                    other.start_col == self.start_col and
                    other.end_col == self.end_col and
                    other.end_row == self.end_row)
        else:
            return False


