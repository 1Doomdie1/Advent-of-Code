def get_input():
    with open('data.txt', 'r') as file:
        data = file.read().split("\n")
    return data


def getStacks():
    data = get_input()[:9]
    stacks = {}
    for col in range(1, len(data[0]), 4):
        temp = [row[col] for row in data[:-1] if row[col].isalpha()]
        stacks[data[-1][col]] = temp[::-1]
    return stacks


def getMoves():
    data = get_input()[10:]
    moves = []
    for i in data:
        temp = i.split(' ')
        moves.append({"amount": int(temp[1]), "from": temp[3], "to": temp[5]})
    return moves


def lastCratesOnStack(stacks):
    creates = [stacks[str(crate)][-1] for crate in range(1, len(stacks) + 1)]
    return ''.join(creates)


def part_one():
    stacks = getStacks()
    moves = getMoves()
    for move in moves:
        moveFrom = stacks[move["from"]]
        amount = move["amount"]
        stacks[move['to']] += moveFrom[-amount:][::-1]
        del stacks[move["from"]][-amount:]
    return lastCratesOnStack(stacks)


def part_two():
    stacks = getStacks()
    moves = getMoves()
    for move in moves:
        moveFrom = stacks[move["from"]]
        amount = move["amount"]
        stacks[move['to']] += moveFrom[-amount:]
        del stacks[move["from"]][-amount:]
    return lastCratesOnStack(stacks)


def main():
    x1 = part_one()
    x2 = part_two()
    print(x1)
    print(x2)


if __name__ == '__main__':
    main()
