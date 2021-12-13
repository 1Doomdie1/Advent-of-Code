with open('data.txt', 'r') as file:
    data = [j.split(' ') for j in [i.replace('\n', ' ')for i in file.read().split('\n\n')]]

def is_valid(p):
    difference = list(set(mandatory_details) - set(p.keys()))
    mandatory_details = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    byr, iyr, eyr, hgt, hcl, ecl, pid = False, False, False, False, False, False, False
    if not len(difference) or difference[0] == 'cid' and len(difference) == 1:
        for key, value in p.items():
            if key == 'byr' and check_dob(value):
                byr = True
            elif key == 'iyr' and check_iyr(value):
                iyr = True
            elif key == 'eyr' and check_eyr(value):
                eyr = True
            elif key == 'hgt' and check_hgt(value):
                hgt = True
            elif key == 'hcl' and check_hcl(value):
                hcl = True
            elif key == 'ecl' and check_ecl(value):
                ecl = True
            elif key == 'pid' and check_pid(value):
                pid = True

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        return True
    return False

def check_dob(v):
    if len(v) == 4 and int(v) >= 1920 and int(v) <= 2002:
        return True

def check_iyr(v):
    if len(v) == 4 and int(v) >= 2010 and int(v) <= 2020:
        return True

def check_eyr(v):
    if len(v) == 4 and int(v) >= 2020 and int(v) <= 2030:
        return True

def check_hgt(v):
    try:
        unit = v[-2:]
        numb = int(v[:-2])
        if unit == 'cm' and numb >= 150 and numb <= 193:
            return True
        elif unit == 'in' and numb >= 59 and numb <= 76:
            return True
    except ValueError:
        return False

def check_hcl(v):
    ltt_and_digits = '0123456789abcdef'
    if v.startswith('#') and len(v) == 7:
        for i in v[1:]:
            if i not in ltt_and_digits:
                return False
                break
        return True

def check_ecl(v):
    eye_cl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if v in eye_cl:
        return True

def check_pid(v):
    if len(v) == 9 and v.startswith('0') or len(v) == 9:
        return True


valid_passports = 0
passports = []
for passport in data:
    details = {}
    for detail in passport:
        key, value = detail.split(':')
        details[key] = value
    passports.append(details)

for i in passports:
    if is_valid(i):
        print(i)
        valid_passports += 1
print(valid_passports)
    