# remaking cs135's sudoku solver in python bc why not
def all_satisfy(pred, matrix):
    return all(all(pred(x) for x in lst) for lst in matrix)

def any_satisfy(pred, matrix):
    return any(any(pred(x) for x in lst) for lst in matrix)

def find_where(pred, matrix):
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if pred(item):
                return (i,j)          
    return None

def find_best(puzzle):
    best_coords = None
    lowest_num = float('inf')
    for i, row in enumerate(puzzle):
        for j, val in enumerate(row):
            if isinstance(val, list):
                if 2 <= len(val) < lowest_num:
                    best_coords = (i,j)
                    lowest_num = len(val)
    return best_coords

def make_copy(puzzle):
    newpuzzle = []
    for row in puzzle:
        new_row = []
        for cell in row:
            if isinstance(cell, list):
                new_row.append(cell.copy())  # Copy the inner list
            else:
                new_row.append(cell)  # ints are immutable, no copy needed
        newpuzzle.append(new_row)
    return newpuzzle

def string_to_puzzle(los):
    def convert(string):
        row = []
        for char in string:
            if char == '?':
                row.append(list(range(1, len(string) + 1)))
            else:
                row.append([(int(char))])
        return row
    finished = []
    for string in los:
        finished.append(convert(string))
    return finished

def remove_singles(puzzle):
    single = find_where(lambda x: isinstance(x, list) and len(x) == 1, puzzle)

    if single is None:
        return puzzle
    single_val = puzzle[single[0]][single[1]][0]
    
    def remove_from_row(val, matrix, row_index):
        for row in matrix:
           if row == matrix[row_index]:
               for item in matrix[row_index]:
                   if isinstance(item, list) and val in item:
                       item.remove(val)
        return matrix
    
    def remove_from_column(val, matrix, col_index):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j == col_index and isinstance(matrix[i][j], list) and val in matrix[i][j]:
                    matrix[i][j].remove(val)
        return matrix
    
    puzzle[single[0]][single[1]] = single_val
    new_puzzle = remove_from_column(single_val, remove_from_row(single_val, puzzle, single[0]), single[1])
    if find_where(lambda x: isinstance(x, list) and len(x) == 1, new_puzzle) is not None:
        remove_singles(new_puzzle)
    return new_puzzle

testing = [[[1], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [2], [1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4], [3], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [4]]]
test1 = string_to_puzzle(["???","?3?","??2"])
test2 = string_to_puzzle(["??3?","??2?","?4??","????"])

def solve_latin(pred, puzzle):
    
    def choice(c):
        return isinstance(c, list) and len(c) >= 2
    
    def solved(puzzle):
        return all_satisfy(lambda x: isinstance(x, int), puzzle)
    
    def contradiction(puzzle):
        return any_satisfy(lambda x: x == [], puzzle)
    
    def try_choices(choices, row, col, puzzle):
        if not choices:
            return False
        newpuzzle = make_copy(puzzle)
        newpuzzle[row][col] = choices[0]
        result = solve_latin(pred, newpuzzle)
        if not result:
            return try_choices(choices[1:], row, col, puzzle)
        return result
    
    simplified = make_copy(puzzle)        
    simplified = remove_singles(simplified)

    if contradiction(simplified):
        return False
    elif solved(simplified):
        if pred(simplified):
            return simplified
        return False
    else:
        coords = find_best(simplified)
        if not coords:
            return False
        row, col = coords
        choices = simplified[row][col]
        return try_choices(choices, row, col, simplified)

puzzle = [[[1, 2, 3, 4], [1, 2, 3, 4], [3], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4], [2], [1, 2, 3, 4]], [[1, 2, 3, 4], [4], [1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]]
#print(solve_latin(lambda x: True, string_to_puzzle(["???","?3?","??2"])))
#print(solve_latin(lambda x: False, string_to_puzzle(["???","?3?","??2"])))        
#print(solve_latin(lambda x: True, string_to_puzzle(["??3?", "??2?", "?4??", "????"])))

def diagonal_has_2(puzzle):
    for i in range(len(puzzle)):
        if puzzle[i][i] == 2:
            return True
    return False
#print(solve_latin(diagonal_has_2, string_to_puzzle(["??3?", "??2?", "?4??", "????"])))
#print(solve_latin(lambda x: False, string_to_puzzle(["??3?", "??2?", "?4??", "????"])))

def sudoku_pred(puzzle):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            newlist = sorted([puzzle[i][j], puzzle[i][j+1], puzzle[i][j+2], puzzle[i+1][j], puzzle[i+1][j+1], puzzle[i+1][j+2], puzzle[i+2][j], puzzle[i+2][j+1], puzzle[i+2][j+2]])
            if newlist != [1,2,3,4,5,6,7,8,9]:
                return False
    return True
print(solve_latin(lambda x: sudoku_pred(x), string_to_puzzle(["48?9?2???","?93??5?86","6??3???1?","???5?1?9?","????9????","?3?2?6???","?7???3??5","24?1??36?","???6?4?27"])))