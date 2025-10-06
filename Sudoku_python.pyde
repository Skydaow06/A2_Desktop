grid = [[0 for _ in range(9)] for _ in range(9)]
cell_size = 80
cell_num = 80

def setup():
    size(1200, 800)
    loadGrid("dataNum.txt")
    
def draw():
    background(255)
    drawGrid()
    gridNumpad()
    drawNumpad()
    drawNumber()

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

def drawNumpad():
    textAlign(CENTER, CENTER)
    textSize(30)
    fill(0)
    numpadNum = 1
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            text(str(numpadNum),
                 (j * cell_num) + 900 + (cell_num / 2),
                 (i * cell_num) + (cell_num / 2) + 280)
            numpadNum += 1
            j += 1
        i += 1
    text("<", 940 + cell_num + cell_num, cell_num * 3)

    
def loadGrid(filename):
    lines = loadStrings(filename)
    
    i = 0
    while(i<9):
        num = split(lines[i], ' ')
        j = 0
        while(j<9):
            grid[i][j] = int(num[j])
            j += 1
        i += 1
        
def drawNumber():
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(0)
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            if grid[i][j] != 0: 
                text(str(grid[i][j]),
                     (j * cell_size) + (cell_size / 2),
                     (i * cell_size) + (cell_size / 2))
            j += 1
        i += 1

        



        
