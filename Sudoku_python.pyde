grid = [[0 for _ in range(9)] for _ in range(9)]
cell_size = 80
cell_num = 80

def setup():
    size(1200, 800)

def draw():
    background(255)
    drawGrid()
    gridNumpad()

def drawGrid():
    i = 0
    while i <= 9:
        line(cell_size * i, 0, cell_size * i, cell_size * 9)
        i += 1
    j = 0
    while j <= 9:
        line(0, cell_size * j, cell_size * 9, cell_size * j)
        j += 1

def gridNumpad():
    i = 0
    while i <= 3:
        line(900 + cell_num * i, 200, 900 + cell_num * i, 200 + cell_num * 4)
        i += 1
    j = 0
    while j <= 4:
        line(900, 200 + cell_num * j, 900 + cell_num * 3, 200 + cell_num * j)
        j += 1
