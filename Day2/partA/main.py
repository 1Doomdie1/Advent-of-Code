with open('data.txt', 'r') as file:
    data = [i.split(' ') for i in file.read().split('\n')]

horizontal = 0
depth = 0

for i in data:
    if i[0] == 'forward':
        horizontal += int(i[1])
    elif i[0] == 'down':
        depth += int(i[1])
    else:
        depth -= int(i[1])
print(horizontal*depth)
