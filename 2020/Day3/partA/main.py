with open('data.txt', 'r') as file:
    data = file.read().split('\n')
trees = 0
column = 0
witdth = len(data[0])
for row in range(len(data)):
    if data[row][column % witdth] == '#':
        trees += 1
    column += 3
print(f'Slope: [3, 1] |Trees count: {trees}')
print(f'Total trees: {trees}')
