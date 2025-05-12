win_char = ''
def win(mat):
    global win_char
    count = 0
    for i in mat:
        if i[0] == i[1] == i[2] and i[0] != ' ':
            win_char = i[0]
            count += 1

    for i in range(3):
        if mat[0][i] == mat[1][i] == mat[2][i] and mat[0][i] != ' ':
            win_char = mat[0][i]
            count += 1

    if mat[0][0] == mat[1][1] == mat[2][2] and mat[0][0] != ' ':
        win_char = mat[0][0]
        count += 1
    elif mat[0][2] == mat[1][1] == mat[2][0] and mat[0][2] != ' ':
        win_char = mat[0][2]
        count += 1

    if win_char != '' and count == 1:
        print(f"{win_char} wins")
    elif count == 0 and (countX +countO) == 9  :
        print("Draw")

def printmat(mat):
    print("---------")
    for l in mat:
        print(f"| {l[0]} {l[1]} {l[2]} |")
    print("---------")

matrix = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
printmat(matrix)
countX = 0
countO = 0
turn_count = 0

cood_index = {(1,1):(0,0),(1,2):(0,1),(1,3):(0,2),(2,1):(1,0),(2,2):(1,1),(2,3):(1,2),(3,1):(2,0),(3,2):(2,1),(3,3):(2,2)}

while True:
    try:
        while turn_count < 9:
            str_cood = input().split()
            (num1, num2) = (int(str_cood[0]), int(str_cood[1]))
            if (num1,num2) in cood_index:
                (x,y) = cood_index[(num1,num2)]
                if matrix[x][y] == 'X' or matrix[x][y] == 'O':
                    print('This cell is occupied! Choose another one!')
                else:
                    if turn_count % 2 == 0:
                        matrix[x][y] = 'X'
                        printmat(matrix)
                        countX += 1
                        turn_count+=1
                    else:
                        matrix[x][y] = 'O'
                        printmat(matrix)
                        countO += 1
                        turn_count += 1
                win(matrix)
            else:
                print("Coordinates should be from 1 to 3!")
            if win_char != '':
                break
    except ValueError :
        print('You should enter numbers!')
    if turn_count == 9:
        break
    elif win_char != '':
        break