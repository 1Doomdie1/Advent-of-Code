
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
    return calories


def part_two():
    calories = part_one()
    top_three = []
    for _ in range(3):
        max_calories = max(calories)
        top_three.append(max_calories)
        calories.pop(calories.index(max_calories))
    return top_three


def main():
    max_calory = max(part_one())
    top_3_calory_sum = sum(part_two())

    print(max_calory)
    print(top_3_calory_sum)


if __name__ == '__main__':
    main()
