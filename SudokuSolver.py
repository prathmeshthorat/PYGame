import sys

sampleInput = '1,0,0,4,8,9,0,0,6,7,3,0,0,5,0,0,4,0,4,6,0,0,0,1,2,9,5,3,8,7,1,2,0,6,0,0,5,0,1,7,0,3,0,0,8,0,4,6,0,9,5,' \
              '7,1,0,9,1,4,6,0,0,0,8,0,0,2,0,0,4,0,0,3,7,8,0,3,5,1,2,0,0,4'


#sys.setrecursionlimit(2500)
resultSet = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def showBoard(sudoku_board):
    countRow = 0
    print('\n')
    for i in sudoku_board:
        countRow = countRow + 1
        row = '| '
        countColumn = 0
        for j in i:
            countColumn = countColumn + 1
            if countColumn % 3 == 0:
                row = row + str(j) + ' | '
            else:
                row = row + str(j) + ' '
        row = row.replace('0', '*', -1)
        print(row[:-1])
        if countRow % 3 == 0 and countRow != 9:
            print('-' * 25)
    print('\n')


def createBoard():
    """inputStream = input('Do you want to input new board ? Yes/No: ')
    if(inputStream.lower()=='no'):
        inputStream = sampleInput
    else:
        inputStream = input('Please input new board: ')
    """
    inputStream = sampleInput
    listOfInts = inputStream.split(',')
    count = 0
    row = []
    board = []
    for i in listOfInts:
        count = count + 1
        if count % 9 == 0:
            row.append(int(i))
            board.append(row)
            row = []
        else:
            row.append(int(i))
    return board


def getEmptyCell(boE):
    for i in range(0, 9):
        for j in range(0, 9):
            if boE[i][j] == 0:
                return i, j


def getColumnValues(boC, i, j):
    lst = []
    for m in range(0, 9):
        if boC[m][j] != 0 and m != i:
            lst.append(boC[m][j])
    return lst


def getRowValues(boR, i, j):
    lst = []
    for m in range(0, 9):
        if boR[i][m] != 0 and m != j:
            lst.append(boR[i][m])
    return lst


def getSquareValues(boS, i, j):
    x = i // 3
    y = j // 3
    lst = []
    # print('x='+str(x)+', y='+str(y))
    for m in range(x * 3, x * 3 + 3):
        for n in range(y * 3, y * 3 + 3):
            # print('m=' + str(m) + ', n=' + str(n)+' boS[m][n]='+str(boS[m][n])+' i='+str(i)+' j='+str(j))
            if boS[m][n] != 0 and not (m == i and n == j):
                lst.append(boS[m][n])
    return lst


def isValid(boV, num, i, j):
    for m in range(0, 9):
        if boV[m][j] == num and m != i:
            return False

        if boV[i][m] == num and m != j:
            return False

    x = i // 3
    y = j // 3
    for m in range(x * 3, x * 3 + 3):
        for n in range(y * 3, y * 3 + 3):
            if boV[m][n] == num and not (m == i and n == j):
                return False

    return True


def solveBoard(sudo):
    if getEmptyCell(sudo) is not None:
        x, y = getEmptyCell(sudo)
    else:
        return True
    for i in resultSet:
        if isValid(sudo, i, x, y):
            sudo[x][y] = i
    if solveBoard(sudo):
        return True
    sudo[x][y] = 0
    return False


if __name__ == "__main__":
    print('\n**Welcome to Sudoku Solver**\n')
    board = createBoard()
    showBoard(board)
    # print(getEmptyCell(board))
    print(solveBoard(board))
    showBoard(board)
