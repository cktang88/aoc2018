import operator

def sortDict(origDict):
    return sorted(origDict.items(), key=operator.itemgetter(1), reverse=True)

def maxDict(origDict):
    k = max(origDict, key=origDict.get)
    return (k, origDict[k])

def minDict(origDict):
    k = min(origDict, key=origDict.get)
    return (k, origDict[k])

with open('7.txt') as f:
    s = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
s = [x.strip().split(' ') for x in s]
s = map(lambda k: (k[1], k[7]), s)

o = dict() # all children
back = dict() # all parents
for i in s:
    (a,b) = i
    if a not in o:
        o[a] = []
    o[a].append(b)
    if b not in back:
        back[b] = []
    back[b].append(a)
print back

boundary = []
exe = ''
for i in o.keys():
    if i not in back:
        boundary.append(i)

done = set() # doneished elems

print boundary

def satisfied(k):
    if k not in back:
        return True
    for i in back[k]:
        if i not in done:
            return False
    return True

times = dict() # keeps times for each task

def cost(k):
    alph = '.abcdefghijklmnopqrstuvwxyz'.upper()
    return alph.index(k)

NUM_WORKERS = 2

workers = []
for i in range(NUM_WORKERS):
    workers.append('')

elapsed = 0

def allDone():
    for i in times.keys():
        if times[i] > 0:
            return False
    return True

while len(boundary) > 0 or not allDone():

    print 'workers: ', workers
    print 'times: ', times
    print 'done: ', done

    # get inext dle
    idle = -1
    for i in workers:
        if i not in times or times[i] <= 0:
            idle = workers.index(i)

    if idle == -1:
        # update time
        elapsed += 1
        for i in times.keys():
            times[i] -= 1
            if times[i] == 0:
                done.add(i)
                exe += i
    
    print 'IDLE', idle
    print exe
    # compute
    
    boundary.sort()
    print 'boundary: ', boundary
    origBoundary = [x for x in boundary] # deepcopy
    e = boundary.pop(0)
    
    cnt = 0
    while e in done or not satisfied(e):
        if len(boundary) == 0:
            break
        e = boundary.pop(0)
        print e
        if not satisfied(e):
            print back[e]
            boundary.append(e) # push to back
        cnt += 1
        if cnt >= len(origBoundary): # just wait if no available task
            boundary = origBoundary
            print 'Reset boundary.'
            break
    
    print idle
    workers[idle] = e
    times[e] = cost(e)


    #print e
    if e in o:
        print 'children: ', o[e]
        for k in o[e]:
            if k not in boundary:
                boundary.append(k)
    boundary = filter(lambda e: e not in done, boundary)
    #print boundary
    if len(boundary) == 0:
        break

print exe

print sortDict(times)
print elapsed


