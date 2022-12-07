import os

with open('data.txt', 'r') as file:
    data = file.read().strip().split('\n')


def makeFs():
    fs = {"subdirs": {}, "dds": {}}
    for line in data:
        if line[0] == '$':
            ds, cmd, *ddir = line.split()
            if cmd == 'cd':
                path = ddir[0]
                if path == '/': 
                    curdir = path 
                else:
                    curdir = os.path.normpath(os.path.join(curdir, path))
                if curdir not in fs["subdirs"]: 
                    fs["subdirs"][curdir] = []
                    fs["dds"][curdir] = 0
        else: 
            fsize, fname = line.split()
            if fsize != 'dir': 
                fs["dds"][curdir] += int(fsize)
            else: 
                fs["subdirs"][curdir].append(os.path.normpath(os.path.join(curdir, fname)))
    return fs


def calculateSize(dirname: str, fs):
    dirsize = fs["dds"][dirname]
    subdirs = fs["subdirs"] 
    for i in subdirs[dirname]: 
        if i in subdirs:
            dirsize += calculateSize(i, fs) 
    return dirsize


def part_one(fs):
    subdirs = fs["subdirs"]
    temp = 0
    for i in subdirs:
        dirsize = calculateSize(i, fs)
        if dirsize <= 100000:
            temp += dirsize
    return temp


def part_two(fs):
    dds = fs["dds"]
    fsSpace = 70000000
    space_required = 30000000
    space_used = calculateSize('/', fs)

    temp = fsSpace
    for i in dds:
        dirsize = calculateSize(i, fs)
        if dirsize >= space_required - (fsSpace - space_used) and dirsize <= temp:
            temp = dirsize
    return temp


def main():
    fs = makeFs()
    x1 = part_one(fs)
    x2 = part_two(fs)
    print(x1)
    print(x2)


if __name__ == '__main__':
    main()
