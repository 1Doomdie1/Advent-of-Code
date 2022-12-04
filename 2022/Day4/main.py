def get_input():
    with open('data.txt', 'r') as file:
        data = file.read().split('\n')
    return parse_data(data)


def parse_data(data):
    temp = [i.replace(",", "-").split('-') for i in data]
    temp = [[int(j) for j in i] for i in temp]
    return temp


def part_one(pairs):
    overlaping_assigments = 0
    for pair in pairs:
        if (pair[0] <= pair[2] and pair[1] >= pair[3]) or (pair[0] >= pair[2] and pair[1] <= pair[3]):
            overlaping_assigments += 1
    return overlaping_assigments 


def part_two(pairs):
    overlaping_assigments = 0
    for pair in pairs:
        set1 = {i for i in range(pair[0], pair[1] + 1)}
        set2 = {i for i in range(pair[2], pair[3] + 1)}
        if len(set1.intersection(set2)) != 0:
            overlaping_assigments += 1
    return overlaping_assigments


def main():
    pairs = get_input()
    x1 = part_one(pairs)
    x2 = part_two(pairs)
    print(x1)
    print(x2)


if __name__ == '__main__':
    main()
