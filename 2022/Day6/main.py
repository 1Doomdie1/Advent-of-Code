def get_input():
    with open('data.txt', 'r') as file:
        data = file.read()
    return data


def part_one():
    datastream = get_input()
    for i in range(len(datastream)):
        window = i + 4
        unique_letters = len(set(datastream[i:window]))
        if len(datastream[i:window]) == 4 and unique_letters == 4:
            return len(datastream[:window])


def part_two():
    datastream = get_input()
    for i in range(len(datastream)):
        window = i + 14
        unique_letters = len(set(datastream[i:window]))
        if len(datastream[i:window]) == 14 and unique_letters == 14:
            return len(datastream[:window])


def main():
    x1 = part_one()
    x2 = part_two()
    print(x1)
    print(x2)


if __name__ == '__main__':
    main()
