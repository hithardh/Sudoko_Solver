board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
	
def solve(boa):
    """
    Solves a sudoku board using backtracking
    :param boa: 2d list of ints
    :return: solution
    """
    find = find_empty(boa)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(boa, (row, col), i):
            boa[row][col] = i

            if solve(boa):
                return True

            boa[row][col] = 0

    return False


def valid(boa, pos, num):
    """
    Returns if the attempted move is valid
    :param boa: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """

    # Check row
    for i in range(0, len(boa)):
        if boa[pos[0]][i] == num and pos[1] != i:
            return False
    # Check Col
    for i in range(0, len(boa)):
        if boa[i][pos[1]] == num and pos[1] != i:
            return False
    # Check box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if boa[i][j] == num and (i,j) != pos:
                return False

    return True


def find_empty(boa):
    """
    finds an empty space in the board
    :param boa: partially complete board
    :return: (int, int) row col
    """

    for i in range(len(boa)):
        for j in range(len(boa[0])):
            if boa[i][j] == 0:
                return (i,j)

    return None


def print_board(boa):
    """
    prints the board
    :param boa: 2d List of ints
    :return: None
    """
    for i in range(len(boa)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(boa[0])):
            if j%3== 0 and j!=0:
                print(" | ",end="")

            if j==8:
                print(boa[i][j], end="\n")
            else:
                print(str(boa[i][j]) + " ", end="")


print_board(board)
solve(board)
print()
print()
print_board(board)				