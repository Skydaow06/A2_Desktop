grid = [[0 for _ in range(9)] for _ in range(9)]
cell_size = 80
cell_num = 80
selectedRow = -1
selectedCol = -1

def setup():
    size(1200, 800)
    loadGrid("dataNum.txt")
    
def draw():
    background(255)
    drawGrid()
    gridNumpad()
    drawNumpad()
    drawNumber()
    drawSelection()

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

def drawSelection():
    if selectedRow != -1 and selectedCol != -1:
        noFill()
        stroke(255, 0, 0)
        strokeWeight(3)
        rect(selectedCol * cell_size, selectedRow * cell_size, cell_size, cell_size)
        strokeWeight(1)
        stroke(0)
        
def mousePressed():
    global selectedRow, selectedCol, grid  
    if mouseX >= 0 and mouseX < cell_size * 9 and mouseY >= 0 and mouseY < cell_size * 9:
        selectedCol = int(mouseX / cell_size)
        selectedRow = int(mouseY / cell_size)
        print("Selected: row=" + str(selectedRow) + ", col=" + str(selectedCol))
        return

    nx = mouseX - 900
    ny = mouseY - 300

    if nx >= 0 and nx < cell_num * 3 and ny >= 0 and ny < cell_num * 3 and selectedRow != -1 and selectedCol != -1:
        colNum = int(nx / cell_num)
        rowNum = int(ny / cell_num)
        num = rowNum * 3 + colNum + 1

        if isValid(selectedRow, selectedCol, num):
            grid[selectedRow][selectedCol] = num
            print("Inserted: " + str(num) + " at row=" + str(selectedRow) + ", col=" + str(selectedCol))
        else:
            print("Cannot insert " + str(num) + " at row=" + str(selectedRow) + ", col=" + str(selectedCol) + " (duplicate!)")

    backX = 940 + cell_num + cell_num
    backY = cell_num * 3
    if mouseX >= backX - 40 and mouseX <= backX + 40 and mouseY >= backY - 40 and mouseY <= backY + 40 and selectedRow != -1 and selectedCol != -1:
        grid[selectedRow][selectedCol] = 0
        print("Deleted at row=" + str(selectedRow) + ", col=" + str(selectedCol))

def isValid(row, col, num):
    i = 0
    while i < 9:
        if grid[row][i] == num:
            return False
        i += 1
    i = 0
    while i < 9:
        if grid[i][col] == num:
            return False
        i += 1
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if grid[startRow + i][startCol + j] == num:
                return False
            j += 1
        i += 1

    return True
