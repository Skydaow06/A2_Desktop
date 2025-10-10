grid = [[0 for _ in range(9)] for _ in range(9)]
cell_size = 80
cell_num = 80
selectedRow = -1
selectedCol = -1
messageText = ""
messageStartTime = 0
fixedCell = [[False for _ in range(9)] for _ in range(9)]
gameWon = False;

def setup():
    size(1200, 750)
    loadGrid("dataNum.txt")

def draw():
    global gameWon
    background(255)
    gridNumpad()
    drawNumpad()
    drawNumber()
    drawGrid() 
    drawSelection()
    drawMessage()  
    
    if isGameComplete():
        gameWon = True

    if gameWon:
        fill(0, 150, 0)
        textSize(40)
        textAlign(CENTER, CENTER)
        text("YOU WON!!", width - 200, height - 650)
    
def drawGrid():
    i = 0
    while i <= 9:
        if i % 3 == 0:
            strokeWeight(4) 
        else:
            strokeWeight(1)
        line(cell_size * i, 0, cell_size * i, cell_size * 9)
        i += 1

    j = 0
    while j <= 9:
        if j % 3 == 0:
            strokeWeight(4)
        else:
            strokeWeight(1)
        line(0, cell_size * j, cell_size * 9, cell_size * j)
        j += 1

    strokeWeight(1)  

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
            text(str(numpadNum), (j * cell_num) + 900 + (cell_num / 2), (i * cell_num) + (cell_num / 2) + 280)
            numpadNum += 1
            j += 1
        i += 1
    text("<", 940 + cell_num + cell_num, cell_num * 3)

def loadGrid(filename):
    lines = loadStrings(filename)
    i = 0
    while i < 9:
        num = split(lines[i], ' ')
        j = 0
        while j < 9:
            grid[i][j] = int(num[j])
            fixedCell[i][j] = (grid[i][j] != 0)
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
                if fixedCell[i][j]:
                    fill(200, 200, 200)
                    rect(j * cell_size, i * cell_size, cell_size, cell_size)
                    fill(0)
                else:
                    fill(0, 0, 200)
                text(grid[i][j], j * cell_size + cell_size / 2, i * cell_size + cell_size / 2)
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
    if (gameWon): return
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
        else:
            warningMessage("Can not insert !!")

    backX = 940 + cell_num + cell_num
    backY = cell_num * 3
    if mouseX >= backX - 40 and mouseX <= backX + 40 and mouseY >= backY - 40 and mouseY <= backY + 40 and selectedRow != -1 and selectedCol != -1:
        grid[selectedRow][selectedCol] = 0
    

def isValid(row, col, num):
    i = 0
    while i < 9:
        if i != col and grid[row][i] == num:
            return False
        if i != row and grid[i][col] == num:
            return False
        i += 1

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    r = 0
    while r < 3:
        c = 0
        while c < 3:
            if ((start_row + r != row or start_col + c != col) and 
                grid[start_row + r][start_col + c] == num):
                return False
            c += 1
        r += 1
    return True

def warningMessage(text):
    global messageText, messageStartTime
    messageText = text
    messageStartTime = millis()

def drawMessage():
    if messageText != "" and millis() - messageStartTime < 2000:
        fill(255, 80, 80)
        textAlign(CENTER, CENTER)
        textSize(40)
        text(messageText, width - 200, height - 650 )
        
def isGameComplete():
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            if grid[i][j] == 0 or not isValid(i, j, grid[i][j]):
                return False
            j += 1
        i += 1
    return True
