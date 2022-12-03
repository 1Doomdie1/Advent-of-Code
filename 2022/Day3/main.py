from string import ascii_letters


def get_input():
    with open('data.txt', 'r') as file:
        data = file.read().split('\n')
    return data


def LettersHashMap():
    '''
    a -> z [1....26]
    A -> Z [26...52]
    '''
    temp = {}
    for index, value in enumerate(ascii_letters, 1):
        temp[value] = index
    return temp


def part_one():
    packs = get_input()
    totalSum = 0
    hashMap = LettersHashMap()
    for pack in packs:
        packLenght = len(pack)
        firtsHalf = set(pack[:packLenght // 2])
        secondHalf = set(pack[packLenght // 2:])
        commonItem = ''.join(firtsHalf & secondHalf)
        totalSum += hashMap[commonItem]
    return totalSum


def part_two():
    packs = get_input()
    hashMap = LettersHashMap()
    groupedPacks = (packs[i:i + 3] for i in range(0, len(packs), 3))
    totalSum = 0
    for group in groupedPacks:
        commonItem = ''.join(set(group[0]) & set(group[1]) & set(group[2]))
        totalSum += hashMap[commonItem]
    return totalSum


def main():
    ex1 = part_one()
    ex2 = part_two()
    print(ex1)
    print(ex2)


if __name__ == '__main__':
    main()
