#Problem: Did I finished my sudoku? (http://www.codewars.com/kata/did-i-finish-my-sudoku)

def rows_are_ok(board):
    rows_ok = [True if len(r) == len(set(r)) else False for r in board]
    return all(rows_ok)

def columns_are_ok(board):
    columns = [list(t) for t in list(zip(*board))]
    columns_ok = [True if len(c) == len(set(c)) else False for c in columns]
    return all(columns_ok)

def boxes_are_ok(board):
    boxes = []
    for r in range(3):
        for c in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[3*r + i][3*c + j])
            boxes.append(block)
    boxes_ok = [True if len(b) == len(set(b)) else False for b in boxes]
    return all(boxes_ok)

def done_or_not(board):
    if rows_are_ok(board) and columns_are_ok(board) and boxes_are_ok(board):
        return 'Finished!'
    return 'Try again!'
