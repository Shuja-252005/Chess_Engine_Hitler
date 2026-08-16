from operator import truediv


class GameState:

    def __init__(self):
        # self.board = \
        #     [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        #               ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        #               ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"], ]
        self.board =  [
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "bK", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "wp", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
]
        self.moveFunction = {"p": self.allPawnMoves, "r": self.allRookMoves, "n": self.allKnightMoves,
                             "b": self.allBishopMoves, "q": self.allQueenMoves, "k": self.allKingMoves}
        self.move_log = []
        self.white_to_move = False
        self.whiteKingPosition = (7,4)
        self.blackKingPosition = (0,4)
        self.isCheckMate = False
        self.isStaleMate = False

    def makeMove(self, move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.white_to_move = not self.white_to_move
        if move.piece_moved == "wk":
            self.whiteKingPosition = (move.end_row,move.end_col)
        elif move.piece_moved == "bK":
            self.blackKingPosition = (move.end_row, move.end_col)


    def undoMove(self):
        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move
            if move.piece_moved == "wk":
                self.whiteKingPosition = (move.start_row, move.start_col)
            elif move.piece_moved == "bK":
                self.blackKingPosition = (move.start_row, move.start_col)

    """Method for all moves with checks and stuff"""

    def getValidMoves(self):
        all_moves = self.getAllPossibleMoves()
        """Whenever removing something from a list always start from the end so that you won't miss an element"""
        for i in range(len(all_moves) - 1,-1,-1):
            self.makeMove(all_moves[i]) # Make the White move (a)
            self.white_to_move = not self.white_to_move
            if self.isCheck():
                del all_moves[i]
            self.white_to_move = not self.white_to_move
            self.undoMove() # Reverse the move you made at (a)
        if len(all_moves) == 0:
            if self.isCheck():
                self.isCheckMate = True
            else:
                self.isStaleMate = True
        else:
            self.isCheckMate = False
            self.isStaleMate = False
        return all_moves


    def isCheck(self):
        if self.white_to_move:
            return self.squareUnderAttack(self.whiteKingPosition)
        else:
            return self.squareUnderAttack(self.blackKingPosition)

    def squareUnderAttack(self,coordinate):
        self.white_to_move = not self.white_to_move
        all_moves = self.getAllPossibleMoves()
        self.white_to_move = not self.white_to_move
        for move in all_moves:  # check if any black move checks white king
            if coordinate == (move.end_row, move.end_col):
                return True
        return False










    """All possible moves"""

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range((len(self.board[r]))):
                if self.white_to_move and self.board[r][c][0] == "w":
                    piece = self.board[r][c]
                    kind = piece[1].lower()
                    self.moveFunction[kind](r, c, moves)
                elif not self.white_to_move and self.board[r][c][0] == "b":
                    piece = self.board[r][c]
                    kind = piece[1].lower()
                    self.moveFunction[kind](r, c, moves)

        return moves

    """All possible pawn moves Shuja"""
    # def allPawnMoves(self, r, c, moves):
    #     piece = self.board[r][c]
    #     color = piece[0]
    #
    #     if color == "w":
    #         first_move = r == 6
    #         if first_move:
    #             """First 1 and 2 moves up straight"""
    #             for i in range(1, 3):
    #                 """check if move within chess boards and on empty square"""
    #                 if self.withInChessBoard(r - i, c) and (self.board[r - i][c] == "--"):
    #                     move = Move((r, c), (r - i, c), self.board)
    #                     moves.append(move)
    #         else:
    #             """Only one move up because already moved"""
    #             if self.withInChessBoard(r - 1, c) and (self.board[r - 1][c] == "--"):
    #                 move = Move((r, c), (r - 1, c), self.board)
    #                 moves.append(move)
    #         """For Left diagonal move"""
    #         if self.withInChessBoard(r - 1, c - 1) and self.board[r - 1][c - 1][0] == "b":
    #             move1 = Move((r, c), (r - 1, c - 1), self.board)
    #             moves.append(move1)
    #         """For Right diagonal move"""
    #         if self.withInChessBoard(r - 1, c + 1) and self.board[r - 1][c + 1][0] == "b":
    #             move2 = Move((r, c), (r - 1, c + 1), self.board)
    #             moves.append(move2)
    #     else:
    #         first_move = r == 1
    #         if first_move:
    #             """First 1 and 2 moves down straight"""
    #             for i in range(1, 3):
    #                 """check if move within chess boards and on empty square"""
    #                 if self.withInChessBoard(r + i, c) and (self.board[r + i][c] == "--"):
    #                     move = Move((r, c), (r + i, c), self.board)
    #                     moves.append(move)
    #         else:
    #             """Only one move up because already moved"""
    #             if self.withInChessBoard(r + 1, c) and (self.board[r + 1][c] == "--"):
    #                 move = Move((r, c), (r + 1, c), self.board)
    #                 moves.append(move)
    #         """For Left diagonal move"""
    #         if self.withInChessBoard(r + 1, c + 1) and self.board[r + 1][c + 1][0] == "w":
    #             move1 = Move((r, c), (r + 1, c + 1), self.board)
    #             moves.append(move1)
    #         """For Right diagonal move"""
    #         if self.withInChessBoard(r + 1, c - 1) and self.board[r + 1][c - 1][0] == "w":
    #             move2 = Move((r, c), (r + 1, c - 1), self.board)
    #             moves.append(move2)

    """All Pawn moves Video"""

    def allPawnMoves(self, r, c, moves):
        if self.white_to_move and self.board[r][c][0] == "w":
            if self.board[r - 1][c] == "--":
                moves.append(Move((r, c), (r - 1, c), self.board))
                if r == 6:
                    if self.board[r - 2][c] == "--":
                        moves.append(Move((r, c), (r - 2, c), self.board))
            if c + 1 < 8:  # right diagonal
                if self.board[r - 1][c + 1][0] == "b":
                    moves.append(Move((r, c), (r - 1, c + 1), self.board))
            if c - 1 >= 0:  # Left diagonal
                if self.board[r - 1][c - 1][0] == "b":
                    moves.append(Move((r, c), (r - 1, c - 1), self.board))
        elif not self.white_to_move and self.board[r][c][0] == "b":
            if self.board[r + 1][c] == "--":
                moves.append(Move((r, c), (r + 1, c), self.board))
                if r == 1:
                    if self.board[r + 2][c] == "--":
                        moves.append(Move((r, c), (r + 2, c), self.board))
            if c - 1 >= 0:  # Left diagonal
                if self.board[r + 1][c - 1][0] == "w":
                    moves.append(Move((r, c), (r + 1, c - 1), self.board))
            if c + 1 < 8:  # Right diagonal
                if self.board[r + 1][c + 1][0] == "w":
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))

    """Shuja Rook Moves"""
    # def allRookMoves(self,r,c,moves):
    #     if self.white_to_move and self.board[r][c][0] == "w":
    #         changing_square = c
    #         while changing_square + 1 < 8:# right Moves
    #             changing_square += 1
    #             if self.board[r][changing_square][0] == "w": #If white pawn dont add that square
    #                 break
    #             elif self.board[r][changing_square][0] == "b": # if black pawn add that move
    #                 moves.append(Move((r, c), (r, changing_square), self.board))
    #                 break
    #             else: # if nothing add that move
    #                 moves.append(Move((r, c), (r, changing_square), self.board))
    #
    #         changing_square = c
    #         while changing_square - 1 >= 0:# Left Moves
    #             changing_square -= 1
    #             if self.board[r][changing_square][0] == "w": #If white pawn dont add that square
    #                 break
    #             elif self.board[r][changing_square][0] == "b": # if black pawn add that move
    #                 moves.append(Move((r, c), (r, changing_square), self.board))
    #                 break
    #             else: # if nothing add that move
    #                 moves.append(Move((r, c), (r, changing_square), self.board))
    #
    #         changing_square = r
    #         while changing_square - 1 >= 0:# Up Moves
    #             changing_square -= 1
    #             if self.board[changing_square][c][0] == "w": #If white pawn dont add that square
    #                 break
    #             elif self.board[changing_square][c][0] == "b": # if black pawn add that move
    #                 moves.append(Move((r, c), (changing_square, c), self.board))
    #                 break
    #             else: # if nothing add that move
    #                 moves.append(Move((r, c), (changing_square, c), self.board))
    #
    #         changing_square = r
    #         while changing_square + 1 < 8:  # Down Moves
    #             changing_square += 1
    #             if self.board[changing_square][c][0] == "w":  # If white pawn dont add that square
    #                 break
    #             elif self.board[changing_square][c][0] == "b":  # if black pawn add that move
    #                 moves.append(Move((r, c), (changing_square, c), self.board))
    #                 break
    #             else:  # if nothing add that move
    #                 moves.append(Move((r, c), (changing_square, c), self.board))
    #
    #     elif not self.white_to_move and self.board[r][c][0] == "b":

    """Video Rook Moves"""

    def allRookMoves(self, r, c, moves):
        direction = ((-1, 0), (1, 0), (0, 1), (0, -1))
        enemy_color = "b" if self.white_to_move else "w"
        for d in direction:
            for i in range(1, 8):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if self.withInChessBoard(end_row, end_col):
                    if self.board[end_row][end_col] == "--":
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif self.board[end_row][end_col][0] == enemy_color:
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                        break
                    else:
                        break  # if a friendly piece present
                else:
                    break  # Off the chess board

    def allBishopMoves(self, r, c, moves):
        direction = ((-1, -1), (1, 1), (1, -1), (-1, 1))  # Top Left, Bottom Right, Bottom Left, Top Right
        enemy_color = "b" if self.white_to_move else "w"
        for d in direction:
            for i in range(1, 8):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if self.withInChessBoard(end_row, end_col):
                    if self.board[end_row][end_col] == "--":
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif self.board[end_row][end_col][0] == enemy_color:
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                        break
                    else:
                        break  # if a friendly piece present
                else:
                    break  # Off the chess board

    def allKnightMoves(self, r, c, moves):
        directions = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))
        for d in directions:
            end_row = r + d[0]
            end_col = c + d[1]
            if self.withInChessBoard(end_row, end_col):
                if self.white_to_move:
                    if self.board[end_row][end_col][0] == "b":
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif self.board[end_row][end_col] == "--":
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                else:
                    if self.board[end_row][end_col][0] == "w":
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif self.board[end_row][end_col] == "--":
                        moves.append(Move((r, c), (end_row, end_col), self.board))

    def allQueenMoves(self, r, c, moves):
        self.allRookMoves(r, c, moves)
        self.allBishopMoves(r, c, moves)

    def allKingMoves(self, r, c, moves):
        directions = ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1))
        if self.white_to_move:
            for d in directions:
                end_row = r + d[0]
                end_col = c + d[1]
                if self.withInChessBoard(end_row,end_col):
                    if self.board[end_row][end_col] == "--":
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif self.board[end_row][end_col][0] == "b":
                        moves.append(Move((r, c), (end_row, end_col), self.board))
        else:
            for d in directions:
                end_row = r + d[0]
                end_col = c + d[1]
                if self.withInChessBoard(end_row,end_col):
                    if self.board[end_row][end_col] == "--":
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif self.board[end_row][end_col][0] == "w":
                        moves.append(Move((r, c), (end_row, end_col), self.board))





    def withInChessBoard(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8


class Move:
    rowsToRank = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
    colsToFiles = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

    def __init__(self, start_pos, end_pos, board):
        self.start_row = start_pos[0]
        self.start_col = start_pos[1]
        self.end_row = end_pos[0]
        self.end_col = end_pos[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

    """The chess notation is the notation for the complete move like (bp at a4 ---- wP at b3"""

    def getChessNotation(self):
        return self.getRankFile(self.start_row, self.start_col) + self.getRankFile(self.end_row, self.end_col)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRank[r]

    def __eq__(self, other):
        if isinstance(other, Move):
            return (other.start_row == self.start_row and
                    other.start_col == self.start_col and
                    other.end_col == self.end_col and
                    other.end_row == self.end_row)
        else:
            return False
