with open('data.txt', 'r') as file:
    data = [i.split(': ') for i in file.read().split('\n')]
good_paswd_cnt = 0
for i in data:
    paswd = i[1]
    min_max = [int(k) for k in i[0].split(' ')[0].split('-')]
    low = min_max[0] - 1
    high = min_max[1] - 1
    ltt = i[0].split(' ')[1]
    if paswd[low] == ltt and paswd[high] != ltt or paswd[low] != ltt and paswd[high] == ltt:
        good_paswd_cnt += 1
print(good_paswd_cnt)
