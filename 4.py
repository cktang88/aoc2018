with open('4.txt') as f:
    s = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
s = [x.strip().split(' ') for x in s]
s.sort()

def getTime(c):
    return int(c[1][3:5])

#print(s)

'''
part 1
'''

guards = dict()
cur = -1
start = -1
for i, c in enumerate(s):
    print c
    if len(c)==6:
        cur = c[3]
    if c[2] == 'falls':
        start = getTime(c)
    if c[2] == 'wakes':
        if cur not in guards.keys():
            guards[cur] = 0
        guards[cur] += getTime(c) - start

print guards
print max(guards, key=guards.get)


# guard 2753
times = dict()
cur = -1
start = -1
for i, c in enumerate(s):
    if len(c)==6:
        cur = c[3]
        total = 0 # reset
    if cur != '#2753':
        continue
    if c[2] == 'falls':
        start = getTime(c)
    if c[2] == 'wakes':
        for k in range(start, getTime(c)):
            if k not in times.keys():
                times[k] = 0
            times[k] += 1
print times
print max(times, key=times.get)


'''
part 2
'''

times = dict()
cur = -1
start = -1
def getTime(c):
    return int(c[1][3:5])
for i, c in enumerate(s):
    if len(c)==6:
        cur = c[3]
        total = 0 # reset
        
    if c[2] == 'falls':
        start = getTime(c)
    if c[2] == 'wakes':
        for k in range(start, getTime(c)):
            if (k,cur) not in times.keys():
                times[(k,cur)] = 0
            times[(k,cur)] += 1

print max(times, key=times.get)


