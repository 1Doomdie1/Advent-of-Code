
def get_input(path):
    with open(path, "r") as file:
        data = file.read().split('\n')
    return data


def part_one():
    calories = []
    temp = 0
    for calory in get_input("data.txt"):
        if calory != '':
            temp += int(calory)
        else:
            calories.append(temp)
            temp = 0
    return max(calories)


def part_two():
    calories = []
    temp = 0
    for calory in get_input("data.txt"):
        if calory != '':
            temp += int(calory)
        else:
            calories.append(temp)
            temp = 0
    top_three = []

    for _ in range(3):
        max_calories = max(calories)
        top_three.append(max_calories)
        calories.pop(calories.index(max_calories))
    return sum(top_three)


def main():
    print(part_one())
    print(part_two())


if __name__ == '__main__':
    main()
