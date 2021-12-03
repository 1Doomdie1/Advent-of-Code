with open('data.txt', 'r') as file:
    data = file.read().split('\n')


def oxygen(d):
    index = 0
    while index < 12:
        col = ''.join([i[index] for i in d])
        zeroes = col.count('0')
        ones = col.count('1')
        x = []
        if ones > zeroes or zeroes == ones:
            for j in d:
                if j[index] == '1':
                    x.append(j)
        else:
            for j in d:
                if j[index] == '0':
                    x.append(j)
        d = x
        index += 1
        if len(d) == 1:
            break
    return int(x[0], 2)


def CO2(d):
    index = 0
    while index < 12:
        col = ''.join([i[index] for i in d])
        zeroes = col.count('0')
        ones = col.count('1')
        x = []
        if ones > zeroes or zeroes == ones:
            for j in d:
                if j[index] == '0':
                    x.append(j)
        else:
            for j in d:
                if j[index] == '1':
                    x.append(j)
        d = x
        index += 1
        if len(d) == 1:
            break
    return int(x[0], 2)


oxygen = oxygen(data)
CO2 = CO2(data)
print(oxygen * CO2)
