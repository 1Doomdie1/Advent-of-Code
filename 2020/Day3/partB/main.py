with open('data.txt', 'r') as file:
	data = file.read().split('\n')

x = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
total_trees = 1
for i in x:
	trees = 0
	column = 0
	witdth = len(data[0])
	for row in range(0, len(data), i[1]):
		if data[row][column % witdth] == '#':
			trees += 1
		column += i[0]
	total_trees *= trees
	print(f'Slope: {i} |Trees count: {trees}')
print(f'Total trees: {total_trees}')