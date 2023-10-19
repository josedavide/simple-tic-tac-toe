# write your code here

X_SYMBOL = "X"
O_SYMBOL = "O"
BLANK_SYMBOL = "_"


def three_symbols_and_equals(word, symbol):
    return len(word) == 3 and all(item == symbol for item in word)


def three_in_a_row(grid, symbol):
    row1 = grid[0:3]
    row2 = grid[3:6]
    row3 = grid[6:9]
    col1 = grid[0:7:3]
    col2 = grid[1:8:3]
    col3 = grid[2::3]
    dia1 = grid[0::4]
    dia2 = grid[2:8:2]

    return (three_symbols_and_equals(row1, symbol)
            or three_symbols_and_equals(row2, symbol)
            or three_symbols_and_equals(row3, symbol)
            or three_symbols_and_equals(col1, symbol)
            or three_symbols_and_equals(col2, symbol)
            or three_symbols_and_equals(col3, symbol)
            or three_symbols_and_equals(dia1, symbol)
            or three_symbols_and_equals(dia2, symbol))


def too_many_symbols(grid):
    x_count = grid.count(X_SYMBOL)
    o_count = grid.count(O_SYMBOL)
    return abs(x_count - o_count) > 1


def evaluate_game_state(grid):
    x_wins = three_in_a_row(grid, X_SYMBOL)
    o_wins = three_in_a_row(grid, O_SYMBOL)

    status = 'Draw'

    if too_many_symbols(grid):
        status = 'Impossible'
    elif x_wins and o_wins:
        status = 'Impossible'
    elif x_wins:
        status = X_SYMBOL + ' wins'
    elif o_wins:
        status = O_SYMBOL + ' wins'
    elif BLANK_SYMBOL in grid:
        status = 'Game not finished'

    return status


def is_invalid_move(row, col):
    return (row < 1
            or row > 3
            or col < 1
            or col > 3)


def row_column_index(row, col):
    return ((row - 1) * 3 + col) - 1


def is_cell_free(grid, row, col):
    index = row_column_index(row, col)
    return grid[index] == BLANK_SYMBOL


def read_user_move(state):
    row, col = input().split()
    try:
        row = int(row)
        col = int(col)
    except (ValueError, TypeError):
        print("You should enter numbers!")
        return read_user_move(state)

    if is_invalid_move(row, col):
        print("Coordinates should be from 1 to 3!")
        return read_user_move(state)
    elif not is_cell_free(state, row, col):
        print("This cell is occupied! Choose another one!")
        return read_user_move(state)

    return row, col


def register_user_move(grid, row, col, symbol):
    index = row_column_index(row, col)
    grid = list(grid)
    grid[index] = symbol
    return ''.join(grid)


def print_grid(grid):
    a = grid[0:3]
    b = grid[3:6]
    c = grid[6:9]

    print("---------")
    print("| " + ' '.join(a) + " |")
    print("| " + ' '.join(b) + " |")
    print("| " + ' '.join(c) + " |")
    print("---------")


grid = BLANK_SYMBOL * 9
print_grid(grid)

symbols = [X_SYMBOL, O_SYMBOL]
for i in range(9):
    row, col = read_user_move(grid)
    grid = register_user_move(grid, row, col, symbols[i % 2])
    print_grid(grid)

    if three_in_a_row(grid, X_SYMBOL):
        print(X_SYMBOL + ' wins')
        break
    elif three_in_a_row(grid, O_SYMBOL):
        print(O_SYMBOL + ' wins')
        break
else:
    print('Draw')







