with open('data.txt', 'r') as file:
	data = [int(i) for i in file.read().split('\n')]
cur = data[0]
cnt = 0
for i in data:
	if i > cur:
		cnt += 1	
	cur = i
print(cnt)