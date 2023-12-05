def get_data():
    with open("data.txt", "r") as file:
        return file.read().split("\n")

def part_one():
    data = get_data()
    total = 0
    for line in data:
        digits = [letter for letter in line if letter.isdigit()]
        if len(digits) > 1:
            total += int(f"{digits[0]}{digits[-1]}")
        elif len(digits) == 1:
            total += int(f"{''.join(digits * 2)}")
    print(total)

def part_two():
    data = get_data()
    word_to_digit = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    total = 0
    for line in data:
        for word, digit in word_to_digit.items():
            line = line.replace(word, f"{word}{digit}{word}")
        digits = [letter for letter in line if letter.isdigit()]
        if len(digits) > 1:
            total += int(f"{digits[0]}{digits[-1]}")
        elif len(digits) == 1:
            total += int(f"{''.join(digits * 2)}")
    print(total)

if __name__ == "__main__":
    part_one()
    part_two()