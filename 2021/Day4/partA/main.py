import numpy as np
with open('data.txt', 'r') as file:
    data = [i.split('\n') for i in file.read().split('\n\n')]
    moves = [int(i) for i in data[0][0].split(',')]


def check_rows(board, numbers):
    for row in range(5):
        diff = list(set(board[row]) - set(numbers))
        if not diff:
            return True


def check_columns(board, numbers):
    board = board.T
    for column in range(5):
        diff = list(set(board[column]) - set(numbers))
        if not diff:
            return True


def board_sum(board, row_or_col, num):
    b_sum = 0
    for i in board:
        diff = list(set(i)-set(row_or_col))
        b_sum += sum(i) - sum(diff)
    return b_sum*num


def create_boards(inp):
    boards = []
    for i in inp[1:]:
        board = []
        for j in i:
            row = [int(k) for k in j.replace('  ', ' ').split()]
            board.append(row)
        boards.append(np.array(board))
    return boards


def main():
    end = 0
    winning_board = []
    boards = create_boards(data)
    print('[+] Boards')
    for i in boards:
        print(i,'\n')
    while True:
        for board in boards:
            if check_rows(board, moves[:end]) or check_columns(board, moves[:end]):
                print(board)
                break
            end += 1
        break



if __name__ == '__main__':
    main()