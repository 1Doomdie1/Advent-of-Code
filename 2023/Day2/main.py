COMBINATIONS = {"red": 12, "green": 13, "blue": 14}

def get_data():
    with open("data.txt", "r") as file:
        return file.read().split("\n")

def part_one():
    data = get_data()
    valid_games_sum = 0
    for id, game in enumerate(data, 1):
        is_valid = all(sum(1 for color, digit in round.items() if COMBINATIONS[color] >= digit) == len(round) for round in process_rounds(game))
        if is_valid:
            valid_games_sum += id
    print(valid_games_sum)

def part_two():
    data = get_data()
    total_sum = 0
    for game in data:
        rounds = process_rounds(game)
        game_value = 1
        for color in COMBINATIONS:
            color_values = [round.get(color, 0) for round in rounds]
            game_value *= max(color_values)
        total_sum += game_value
    print(total_sum)


def process_rounds(game):
    return [{color_number.split()[1]: int(color_number.split()[0]) for color_number in item.split(', ')} for item in game[game.index(":") + 2:].split("; ")]

if __name__ == "__main__":
    part_one()
    part_two()
