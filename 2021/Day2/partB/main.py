with open('data.txt', 'r') as file:
    data = [i.split(' ') for i in file.read().split('\n')]
aim = 0
depth = 0
horizontal = 0

for i in data:
    if i[0] == 'forward':
        horizontal += int(i[1])
        depth += aim * int(i[1])
    elif i[0] == 'down':
        aim += int(i[1])
    else:
        aim -= int(i[1])
    # print(f'Aim: {aim} | Depth: {depth}')
print(f'Aim: {aim} | Depth: {depth} | Horizontal: {horizontal} | Course: {horizontal*depth}')
