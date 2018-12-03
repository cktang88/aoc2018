with open('3.txt') as f:
    s = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
s = [x.strip().split('@') for x in s]

print(s)
for i, c in enumerate(s):
    a = []
    a.extend(c[1].strip().split(':'))
    s[i] = a
print(s)

sq = [[0 for i in range(1000)] for j in range(1000)]

for i in s:
    x,y = [int(x) for x in i[0].split(',')]
    w,h = [int(q) for q in i[1].split('x')]
    # print x,y,w,h
    for j in range(x, x+w):
        for k in range(y, y+h):
            sq[j][k] += 1

# part2
for i in s:
    x,y = [int(x) for x in i[0].split(',')]
    w,h = [int(q) for q in i[1].split('x')]
    # print x,y,w,h
    ones = True
    for j in range(x, x+w):
        for k in range(y, y+h):
            if sq[j][k] != 1:
                ones = False
                break
        if not ones:
            break
    if ones:
        print x,y,w,h

'''
# part 1
print sq[3]
cnt = 0
for row in sq:
    for j in row:
        if j > 1:
            cnt += 1
print cnt
'''