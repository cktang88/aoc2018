with open('2.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]


'''
# part1
twos = 0
threes = 0
for line in content:
    d = dict()
    for s in line:
        if s not in d:
            d[s] = 0
        d[s] += 1
    hastwo = False
    hasthree = False
    for k in d.keys():
        if d[k] == 2:
            hastwo = True
        if d[k] == 3:
            hasthree = True
    if hastwo:
        twos += 1
    if hasthree:
        threes += 1

print(twos, threes)
'''
# part2
for i in content:
    for j in content:
        cnt = 0
        for k in range(len(i)):
            if i[k] != j[k]:
                cnt += 1
        if cnt == 1:
            print i, j
    