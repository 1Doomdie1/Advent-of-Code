with open('data.txt', 'r') as file:
    data = file.read().split('\n')


def calculate_row(row):
    lower = 0
    upper = 127
    for i in range(6):
        half = (lower + upper) // 2
        if row[i] == 'F':
            upper = half
        elif row[i] == 'B':
            lower = half + 1
    if row[6] == 'F':
        return lower
    return upper


def calculate_col(seat):
    upper = 7
    lower = 0
    for i in range(2):
        half = (lower + upper) // 2
        if seat[i] == 'L':
            upper = half
        elif seat[i] == 'R':
            lower = half + 1
    if seat[2] == 'L':
        return lower
    return upper


ids = []
for seat in data:
    row = calculate_row(seat[:7])
    col = calculate_col(seat[7:])
    seat_id = row * 8 + col
    ids.append(seat_id)
    print(f'Row: {row} | Col: {col} | Seat ID: {seat_id}')

missing_seat = 0
for id_ in ids:
    if id_ + 1 not in ids and id_ + 2 in ids:
        missing_seat = id_ + 1
print(missing_seat)
