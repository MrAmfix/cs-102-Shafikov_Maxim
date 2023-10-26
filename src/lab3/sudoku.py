import random


def read_sudoku(path: str) -> list:
    file = open(path)
    grid = [list(file.readline().rstrip()) for i in range(0, 9)]
    return grid


def get_line(grid: list, n: int) -> list:
    return grid[n]


def get_line_by_pos(grid: list, pos: (int, int)) -> list:
    """Возвращает все значения для номера строки, указанной в pos
        >>> get_line_by_pos([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
        ['1', '2', '.']
        >>> get_line_by_pos([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
        ['4', '.', '6']
        >>> get_line_by_pos([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
        ['.', '8', '9']
        """
    return grid[pos[0]]


def get_column(grid: list, n: int) -> list:
    s = ""
    for i in range(0, 9):
        s += grid[i][n]
    return list(s)


def get_column_by_pos(grid: list, pos: (int, int)) -> list:
    """Возвращает все значения для номера столбца, указанного в pos
        >>> get_column_by_pos([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
        ['1', '4', '7']
        >>> get_column_by_pos([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
        ['2', '.', '8']
        >>> get_column_by_pos([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
        ['3', '6', '9']
        """
    s = []
    for i in range(0, len(grid)):
        s.append(grid[i][pos[1]])
    return s


def get_square(grid: list, n: int) -> list:
    s = []
    for i in range(n // 3 * 3, (n // 3 + 1) * 3):
        for j in range(n % 3 * 3, (n % 3 + 1) * 3):
            s.append(grid[i][j])
    return s


def get_square_by_pos(grid: list, pos: (int, int)) -> list:
    """Возвращает все значения из квадрата, в который попадает позиция pos
        >>> grid = read_sudoku('puzzle1.txt')
        >>> get_square_by_pos(grid, (0, 1))
        ['5', '3', '.', '6', '.', '.', '.', '9', '8']
        >>> get_square_by_pos(grid, (4, 7))
        ['.', '.', '3', '.', '.', '1', '.', '.', '6']
        >>> get_square_by_pos(grid, (8, 8))
        ['2', '8', '.', '.', '.', '5', '.', '7', '9']
        """
    return get_square(grid, (pos[0] // 3) * 3 + (pos[1] // 3))


def group(grid: list, n: int) -> list:
    """
        Сгруппировать значения values в список, состоящий из списков по n элементов
        >>> group([1,2,3,4], 2)
        [[1, 2], [3, 4]]
        >>> group([1,2,3,4,5,6,7,8,9], 3)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        """
    arr = []
    for i in range(n):
        curr = []
        for j in range(n):
            curr.append(grid[i*n+j])
        arr.append(curr)
    return arr


def find_possible_values(grid: list, pos: (int, int)) -> set:
    """Вернуть множество возможных значения для указанной позиции
        >>> grid = read_sudoku('puzzle1.txt')
        >>> values = find_possible_values(grid, (0,2))
        >>> values == {'1', '2', '4'}
        True
        >>> values = find_possible_values(grid, (4,7))
        >>> values == {'2', '5', '9'}
        True
        """
    val = []
    for j in range(1, 10):
        i = str(j)
        if i not in get_line_by_pos(grid, pos) and i not in get_column_by_pos(grid, pos) and i not in get_square_by_pos(grid, pos):
            val.append(str(i))
    return set(val)


def find_empty_positions(grid: list) -> (int, int):
    """Найти первую свободную позицию в пазле
        >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
        (0, 2)
        >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
        (1, 1)
        >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
        (2, 0)
        """
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == '.':
                return (i, j)
    return (-1, -1)


def is_possible_number(grid: list, i_line: int, j_column: int, num: str) -> bool:
    if num in get_line_by_pos(grid, (i_line, j_column)) or num in get_column_by_pos(grid, (i_line, j_column)) or num in get_square_by_pos(grid, (i_line, j_column)):
        return False
    return True


def is_correct_answer(grid: list) -> bool:
    for i_line in range(0, len(grid)):
        for j_column in range(0, len(grid[i_line])):
            if grid[i_line][j_column] == '.':
                return False
            else:
                copy_grid = []
                for i in grid:
                    copy_line = []
                    for j in i:
                        copy_line.append(j)
                    copy_grid.append(copy_line)
                copy_grid[i_line][j_column] = '.'
                if not is_possible_number(copy_grid, i_line, j_column, grid[i_line][j_column]):
                    return False
    return True


def is_correct_sudoku(grid: list) -> bool:
    for i_line in range(0, len(grid)):
        for j_column in range(0, len(grid[i_line])):
            if grid[i_line][j_column] != '.':
                copy_grid = []
                for i in grid:
                    copy_line = []
                    for j in i:
                        copy_line.append(j)
                    copy_grid.append(copy_line)
                copy_grid[i_line][j_column] = '.'
                if not is_possible_number(copy_grid, i_line, j_column, grid[i_line][j_column]):
                    return False
    return True


def sudoku_solve(grid: list) -> bool:
    for i_line in range(9):
        for j_column in range(9):
            if grid[i_line][j_column] == '.':
                for num in range(1, 10):
                    if is_possible_number(grid, i_line, j_column, str(num)):
                        grid[i_line][j_column] = str(num)
                        if sudoku_solve(grid):
                            return True
                        else:
                            grid[i_line][j_column] = '.'
                return False
    return True


def get_solve(grid: list) -> list:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    sudoku_solve(grid)
    return grid


def print_grid(grid: list):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(grid[i][j], end=" ")
        print()


def generate_sudoku(n: int) -> list:
    """Генерация судоку заполненного на N элементов
        >>> grid = generate_sudoku(40)
        >>> sum(1 for row in grid for e in row if e == '.')
        41
        >>> solution = get_solve(grid)
        >>> is_correct_answer(solution)
        True
        >>> grid = generate_sudoku(1000)
        >>> sum(1 for row in grid for e in row if e == '.')
        0
        >>> solution = get_solve(grid)
        >>> is_correct_answer(solution)
        True
        >>> grid = generate_sudoku(0)
        >>> sum(1 for row in grid for e in row if e == '.')
        81
        >>> solution = get_solve(grid)
        >>> is_correct_answer(solution)
        True
        """
    grid = [list('.'*9) for i in range(9)]
    grid = get_solve(grid)
    def swap_line_small(grid: list, line1: int, line2: int) -> list:
        grid[line1], grid[line2] = grid[line2], grid[line1]
        return grid
    def swap_column_small(grid: list, column1: int, column2 : int) -> list:
        for i in range(0, 9):
            grid[i][column1], grid[i][column2] = grid[i][column2], grid[i][column1]
        return grid
    def swap_line_big(grid: list, line1: int, line2: int) -> list:
        grid[line1 * 3], grid[line1 * 3 + 1], grid[line1 * 3 + 2], grid[line2 * 3], grid[line2 * 3 + 1], grid[line2 * 3 + 2] = grid[line2 * 3], grid[line2 * 3 + 1], grid[line2 * 3 + 2], grid[line1 * 3], grid[line1 * 3 + 1], grid[line1 * 3 + 2]
        return grid

    def swap_column_big(grid: list, column1: int, column2: int) -> list:
        for i in range(0, 9):
            grid[i][column1 * 3], grid[i][column1 * 3 + 1], grid[i][column1 * 3 + 2], grid[i][column2 * 3], grid[i][column2 * 3 + 1], grid[i][column2 * 3 + 2] = grid[i][column2 * 3], grid[i][column2 * 3 + 1], grid[i][column2 * 3 + 2], grid[i][column1 * 3], grid[i][column1 * 3 + 1], grid[i][column1 * 3 + 2]
        return grid

    for i in range(0, 3):
        mult = random.randint(0, 2)
        grid = swap_line_small(grid, mult * 3 + random.randint(0, 2), mult * 3 + random.randint(0, 2))
    for i in range(0, 3):
        mult = random.randint(0, 2)
        grid = swap_column_small(grid, mult * 3 + random.randint(0, 2), mult * 3 + random.randint(0,2))
    for i in range(0, 3):
        grid = swap_line_big(grid, random.randint(0, 2), random.randint(0, 2))
    for i in range(0, 3):
        grid = swap_column_big(grid, random.randint(0, 2), random.randint(0, 2))

    pos = []
    for i in range(0, 9):
        for j in range(0, 9):
            pos.append((i, j))
    random.shuffle(pos)
    if n > 81:
        n = 81
    for i in range(0, 81 - n):
        grid[pos[i][0]][pos[i][1]] = '.'
    return grid


if __name__ == "__main__":
    path = "puzzle3.txt"
    grid = read_sudoku(path)
    if not is_correct_sudoku(grid):
        print(f"Puzzle {path} can't be solved")
    else:
        print_grid(get_solve(grid))