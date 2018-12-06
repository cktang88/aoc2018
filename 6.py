import operator

with open('6.txt') as f:
    s = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
s = [[int(k) for k in x.strip().split(',')] for x in s]

maxx = max(s, key=lambda e:e[0])[0]
maxy = max(s, key=lambda e:e[1])[1]
minx = min(s, key=lambda e:e[0])[0]
miny = min(s, key=lambda e:e[1])[1]

print(s)
print maxx, minx, maxy, miny

def mandist(x,y,pt):
    return abs(x-pt[0]) + abs(y-pt[1])

def closest(x,y,s):
    nearest_pt = min(s, key=lambda e: mandist(x,y,e))
    return filter(lambda e: mandist(x,y,e)==mandist(x,y,nearest_pt), s)

'''
partA
'''
def getAreas(border):
    areas = dict()
    for i in range(minx - border, maxx + border):
        print i
        for j in range(miny - border, maxy + border):
            # for each (i,j), find closest pt, border of maxx, maxy
            pt = closest(i,j,s)
            if len(pt) != 1: # belong to no pt
                continue
            pt = str(pt[0])
            #print pt
            if pt not in areas:
                areas[pt] = 0
            areas[pt] += 1

    return areas

a = getAreas(0)
b = getAreas(1)
goodmap = dict()
for i in a.keys():
    if a[i] == b[i]: # find values that stayed same = non-infinite
        goodmap[i] = a[i]

sortedmap = sorted(goodmap.items(), key=operator.itemgetter(1), reverse=True)
print sortedmap[0]

'''
part B
'''
area = 0
for i in range(minx, maxx):
    print i
    for j in range(miny, maxy):
        total = 0
        for k in s:
            total += mandist(i,j,k)
        if total < 10000:
            area += 1
print area

