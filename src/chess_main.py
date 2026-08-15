import pygame as p

from src import chess_engine

WIDTH = HEIGHT = 512
DIMENSIONS = 8
SQ_SIZE = HEIGHT // DIMENSIONS
IMAGES = {}
MAX_FPS = 15

def loadImages():
    pieces = ["wr","wn","wb","wq","wk","wp","bR","bN","bB","bQ","bK","bP"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"),(SQ_SIZE,SQ_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chess_engine.GameState()
    running = True
    validMoves = gs.getValidMoves()

    loadImages()
    square_selected = ()
    """This will contain max of two elements which tell what was the first click and the second,
    first will be the piece one and the second where you need to move it"""
    player_click = []

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #key handler
            if e.type == p.KEYDOWN:
                if e.key == p.K_LEFT:
                    gs.undoMove()
            #mouse handler
            if e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #Exact coordinate of mouse click
                col = location[0] // SQ_SIZE #64 pixel x axis
                row = location[1] // SQ_SIZE #64 pixel x axis
                """Checks if double clicked means if you click piece twice it deselects"""
                if square_selected == (row,col):
                    square_selected = ()
                    player_click = []
                else:
                    square_selected = (row,col)
                    player_click.append(square_selected)
                if len(player_click) == 2:
                    move = chess_engine.Move(player_click[0],player_click[1],gs.board)
                    gs.makeMove(move)
                    print(move.getChessNotation())
                    player_click = []
                    square_selected = ()

        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen,gs):
    drawBoard(screen)
    drawPieces(gs.board,screen)


def drawPieces(board,screen):
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))



def drawBoard(screen):
    colors = [p.Color("white"),p.Color("light blue")]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            # all light square sum of coordinates are even number and dark squares are odd
            if (r+c) % 2 == 0:
                color = colors[0]
            else:
                color = colors[1]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))



if __name__ == "__main__":
    main()