
with open('12.txt') as f:
    s = f.readlines()

s = [x.strip().split(' => ') for x in s]
print s
def process(e):
    return e
    # e = e[10:]
    # k = e.split('>')
    # a = [int(e) for e in k[0].split(',')]
    # b = [int(e) for e in k[1][12:].split(',')]
    # return a,b

s = map(process, s)

mp = {}
for i in s:
    mp[i[0]] = i[1]

#print mp, len(mp.keys())

NUMGENS = 300

buffer = '.'*100

state = buffer + '###......#.#........##.###.####......#..#####.####..#.###..#.###.#..#..#.#..#..#.##...#..##......#.#' + buffer*3
#state = '...#..#.#..##......###...###......................'

#print state

def sumplants(s):
    total = 0
    for i in range(len(s)):
        if s[i] == '#':
            #print i - len(buffer)
            total += i - len(buffer)
    return total

results = []

lastsum = sumplants(state)
print lastsum

for k in range(NUMGENS):
    if k > 1000:
        print k
    tmp = state
    for i in range(2, len(state)-2):
        #print tmp
        c = state[i-2:i+3]
        new = mp[c] if c in mp else '.'
        tmp = tmp[:i] + new + tmp[i+1:]
        #print tmp
        
    state = tmp
    if k > 130:
        print state [len(buffer) - 10: len(buffer) + 500]
    print sumplants(state),k
    # s = sumplants(state)
    # if s in results:
    #     print s, results.index(s), k
    # results.append(s)

print results




