with open('data.txt', 'r') as file:
    data = [int(i) for i in file.read().split('\n')]
for i in data:
    for j in data:
        for k in data:
            if i + j + k == 2020:
                print(i*j*k)