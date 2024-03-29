def get_input():
    with open('data.txt', 'r') as file:
        data = file.read().split('\n')
    return data


def part_one(gameState, gameChoicePoints):
    game = {"A": {"Y": {"Points": gameState["Win"], "Choice Points": gameChoicePoints["B"]},
                  "X": {"Points": gameState["Draw"], "Choice Points": gameChoicePoints["A"]},
                  "Z": {"Points": gameState["Lose"], "Choice Points": gameChoicePoints["C"]}},
            "B": {"Y": {"Points": gameState["Draw"], "Choice Points": gameChoicePoints["B"]},
                  "X": {"Points": gameState["Lose"], "Choice Points": gameChoicePoints["A"]},
                  "Z": {"Points": gameState["Win"], "Choice Points": gameChoicePoints["C"]}},
            "C": {"Y": {"Points": gameState["Lose"], "Choice Points": gameChoicePoints["B"]},
                  "X": {"Points": gameState["Win"], "Choice Points": gameChoicePoints["A"]},
                  "Z": {"Points": gameState["Draw"], "Choice Points": gameChoicePoints["C"]}}}
    return game


def part_two(gameState, gameChoicePoints):
    game = {"A": {"Y": {"Points": gameState["Draw"], "Choice Points": gameChoicePoints["A"]},
                  "X": {"Points": gameState["Lose"], "Choice Points": gameChoicePoints["C"]},
                  "Z": {"Points": gameState["Win"], "Choice Points": gameChoicePoints["B"]}},
            "B": {"Y": {"Points": gameState["Draw"], "Choice Points": gameChoicePoints["B"]},
                  "X": {"Points": gameState["Lose"], "Choice Points": gameChoicePoints["A"]},
                  "Z": {"Points": gameState["Win"], "Choice Points": gameChoicePoints["C"]}},
            "C": {"Y": {"Points": gameState["Draw"], "Choice Points": gameChoicePoints["C"]},
                  "X": {"Points": gameState["Lose"], "Choice Points": gameChoicePoints["B"]},
                  "Z": {"Points": gameState["Win"], "Choice Points": gameChoicePoints["A"]}}}
    return game


def main():
    gameState = {"Lose": 0, "Draw": 3, "Win": 6}
    gameChoicePoints = {"A": 1, "B": 2, "C": 3}

    game_rules = part_one(gameState, gameChoicePoints), part_two(gameState, gameChoicePoints)
    matches = [i.split(' ') for i in get_input()]

    for game in game_rules:
        total_score = 0
        for match in matches:
            total_score += game[match[0]][match[1]]["Points"] + game[match[0]][match[1]]["Choice Points"]
        print(total_score)


if __name__ == '__main__':
    main()
