with open('data.txt', 'r') as file:
	data = [int(i) for i in file.read().split('\n')]
current = sum(data[:3])
cnt = 0
for i in range(len(data)):
	x = data[i:i+3]
	if len(x) == 3:
		sum_ = sum(x) 
		if sum_ > current:
			cnt +=1
		current = sum_
	else:
		break
print(cnt)