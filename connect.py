MAXX = 5
def welcome():
    print("Welcome to Connect Four\nCoded by Itay Tamary\n")
    print("This game is for two players")
    load = ""
    while load != "y" and load != "n":
        load = input("Would you like to load from a save (y/n)? ")
    if load == "y":
        name = input("What game file would you like to load from? ")
        name = name + ".txt"
        first = open(name)
        saved = first.read()
        stringBoard, row, column, index = saved.split(":")
        row = int(row)
        column = int(column)
        index = int(index)
        stringBoard = stringBoard.split("'")
        board = []
        for i in range(len(stringBoard)) :
            if len(stringBoard[i]) > 4 :
                board.append(stringBoard[i])
        return load, board, row, column, index
    elif load == "n" :
        return load, True, True, True, True
    first.close()
def rowsColumns():
    rows = 0
    columns = 0
    msg = "Please enter a number greater or equal to " + str(MAXX) + ": "
    while rows < MAXX :
        print("Please choose the number of rows: ")
        rows = int(input(msg))
    while columns < MAXX :
        print("Please choose the number of column: ")
        columns = int(input(msg))
    return rows, columns

def gameBoard (rows, columns):
    gameBox = []
    piece = "- "
    for i in range(rows):
        board = piece * columns
        gameBox.append(board)
    return gameBox

def gameFunction(symbol, row, column, board, index):
    msg = "Please choose a column to place your piece in (1 - " + str(column) + ") or s to save: "
    modColumn = column - 1
    modRow = row - 1
    choice = input(msg)
    while choice == "s" :
        gameSave(board, row, column, index)
        choice = input(msg)
    choice = int(choice)
    while choice < 1 or choice > column :
        choice = input(msg)
        while choice == "s":
            gameSave(board, row, column, index)
            choice = input(msg)
        choice = int(choice)
    choice = (choice  * 2) - 1
    place = choice - 1
    while board[0][place] != "-" :
        print("That column is full")
        choice = input(msg)
        while choice == "s" :
            gameSave(board, row, column, index)
            choice = input(msg)
        choice = int(choice)
        while choice < 1 or choice > column:
            choice = input(msg)
            while choice == "s" :
                gameSave(board, row, column, index)
                choice = input(msg)
            choice = int(choice)
        choice = (choice * 2) - 1 
        place = choice - 1     
    while board[modRow][place] != "-" :
        modRow = modRow - 1
    if board[modRow][place] == "-":
        board[modRow] = board[modRow][:place] + symbol + board[modRow][choice:]
    
    for i in range(len(board)):
        print(board[i])
    return board
def winCheck (board, symbol, column, row) :
    vert = []
    forDiagList = []
    backDiagList = []
    diag = []
    column = (column * 2) - 1
    horiCheck = symbol + " " + symbol + " " + symbol + " " + symbol
    if symbol == "x":
        vertCheck = "'x', 'x', 'x', 'x'"
    elif symbol == "o" :
        vertCheck = "'o', 'o', 'o', 'o'"
    for i in range(len(board)) :
       
        if (horiCheck in board[i]) == True :
        
            return True
    for i in range(column):
        for n in range(len(board)) :
            
            vert.append(board[n][i])
            
    vert = str(vert)
    if (vertCheck in vert) == True :
        return True

    index = 0
    row = row

                
    for x in range(len(board)-1, 2, -1):
        for y in range(column-6):
            if board[x][y] == symbol and board[x-1][y+2] == symbol and board[x-2][y+4] == symbol and board[x-3][y+6] == symbol  :
                return True
            
            

    for x in range(len(board)-3) :
        for y in range(column-6) :
            if board[x][y] == symbol and board[x+1][y+2] == symbol and board[x+2][y+4] == symbol and board[x+3][y+6] == symbol:
                return True
                
    
        
        
        
    
    return False
    


def gameSave(board, row, column, index):
    board = str(board)
    fileName = input("What would you like to name the saved file? ")
    fileName = fileName + ".txt"
    gameSave = open(fileName, "w")
    gameSave.write(board[1:-1] + ":" + str(row) + ":" + str(column) + ":" + str(index))
    print("File Saved")
def playAgain():
    again = ""
    while again != "y" and again != "n" :
        again = input("Do you want to play again (y/n)? ")
    if again == "y" :
        main()
    else:
        print("Good-bye!")
def main():
    load, board, row, column, index = welcome()
    if load == "n" :
        row, column = rowsColumns()
        board = gameBoard(row, column)
        index = 1
    player1 = "x"
    player2 = "o"
    drawMark = (row * column) + 1
    result = True
    win = False
    winner = ""
    rand = ""
    for i in range(len(board)):
        print(board[i])
    while result == True and win == False :
        if index % 2 != 0 or index == 1 and result == True and win == False:
            print("Player 1 what is your choice?")
            board = gameFunction(player1 , row, column, board, index)
            index = index + 1
            result = "-" in board[0]
            win = winCheck(board, player1, column, row)
            if win == True:
                winner = "Player 1"
                
        if index % 2 == 0 and result == True and win == False:
            print("Player 2 what is your choice?")
            board = gameFunction(player2, row, column, board, index)
            index = index + 1
            result = "-" in board[0]
            win = winCheck(board, player2, column, row)
            if win == True :
                winner = "Player 2"
    if result == False :
        print("Draw")
    elif win == True :
        print(winner, "wins!")
    playAgain()
    
main()

        
