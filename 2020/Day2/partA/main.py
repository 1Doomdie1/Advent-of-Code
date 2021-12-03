with open('data.txt', 'r') as file:
	data = [i.split(': ') for i in file.read().split('\n')]
good_paswd_cnt = 0
for i in data:
	password = i[1]
	min_max = [int(j) for j in i[0].split(' ')[0].split('-')]
	ltt = [k for k in i[0].split(' ')[1]][0]
	low = min_max[0]
	high = min_max[1]
	paswd_lt_cnt = password.count(ltt)
	if paswd_lt_cnt >= low and paswd_lt_cnt <= high:
		print(f'Range: {min_max} | Letter: {ltt} | Password: {password} | Letter count: {paswd_lt_cnt}')
		good_paswd_cnt += 1
print(f'Good passwords: {good_paswd_cnt}')