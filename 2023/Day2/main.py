def get_data():
    with open("data.txt", "r") as file:
        return file.read().split("\n")
