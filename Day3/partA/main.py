with open('data.txt', 'r') as file:
	data = file.read().split('\n')

cnt = 0
gama_rate = ''
epsilon = ''
for i in range(len(data[0])):
	str_ = ''
	for j in range(len(data)):
		str_ += data[j][i]
	zeros = str_.count('0')
	ones = str_.count('1')
	if zeros > ones:
		gama_rate += '0'
		epsilon += '1'
	else:
		gama_rate += '1'
		epsilon += '0'

print(int(gama_rate,2)*int(epsilon, 2))