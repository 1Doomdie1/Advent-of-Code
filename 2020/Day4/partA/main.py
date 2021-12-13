with open('data.txt', 'r') as file:
    data = [j.split(' ') for j in [i.replace('\n', ' ')for i in file.read().split('\n\n')]]

mandatory_details = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
valid_passports = 0

for passport in data:
    details = [detail[:3] for detail in passport]
    difference = list(set(mandatory_details) - set(details))
    if not len(difference) or difference[0] == 'cid' and len(difference) == 1:
        valid_passports += 1

print(f'Valid Pasports: {valid_passports}')